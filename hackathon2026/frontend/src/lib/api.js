import { uid } from "@/lib/mockApi"

// Base URL for the FastAPI backend. Override with VITE_API_BASE_URL in .env.
export const API_BASE_URL =
  import.meta.env?.VITE_API_BASE_URL || "http://127.0.0.1:8000"

// Set VITE_USE_MOCK=true (or hardcode true here) to use the built-in mock
// responses from mockApi.js instead of hitting the real backend.
export const USE_MOCK = import.meta.env?.VITE_USE_MOCK === "true"

const BOOKING_ENDPOINT = "/api/v1/booking"

// POST the prompt to the backend and map the reply into a frontend message.
export async function sendPrompt(prompt) {
  const response = await fetch(`${API_BASE_URL}${BOOKING_ENDPOINT}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  })

  if (!response.ok) {
    throw new Error(`API responded ${response.status} ${response.statusText}`)
  }

  const envelope = await response.json()
  return mapResponseToMessage(envelope)
}

// Maps the backend ApiResponse envelope { status, response, response_time_ms }
// into the frontend message shape consumed by AssistantMessage.
//
// IMPORTANT: the response *variant* is decided by `response.flow`
// (booking | casual) — NOT by `response.router.type`, which only reports which
// router decided (openai_agent | local_fallback) and is the same across
// variants. Within casual, we show a KB answer when RAG produced citable
// content, otherwise plain text.
export function mapResponseToMessage(envelope) {
  const payload = envelope?.response ?? {}

  if (payload.flow === "booking") {
    return {
      id: uid(),
      role: "assistant",
      type: "booking",
      booking: mapBookingPayload(payload),
    }
  }

  // casual: KB answer if RAG returned citable content, else plain text.
  const rag = payload.rag
  const hasKbAnswer = Boolean(
    rag && rag.configured && (rag.chunks?.length || rag.citations?.length)
  )

  if (hasKbAnswer) {
    return {
      id: uid(),
      role: "assistant",
      type: "kb",
      content: rag.answer ?? "",
      sources: dedupeSources(rag.chunks),
    }
  }

  return {
    id: uid(),
    role: "assistant",
    type: "text",
    content: rag?.answer || payload.answer || payload.message || "",
  }
}

// Maps a booking-flow payload { flow, step, message, steps: [...] } into the shape
// BookingStepResponse renders: one summary per executed step, plus the raw
// request/response for the last step only (the one it stopped at).
function mapBookingPayload(payload) {
  const entries = payload.steps ?? []

  const steps = entries.map((entry) => ({
    step: entry.step,
    status: entry.status,
    message: entry.message,
    data: summarizeBookingData(entry.step, entry),
  }))

  const last = entries[entries.length - 1]
  const requestResponse =
    last && (last.request || last.response)
      ? { step: last.step, request: last.request ?? null, response: last.response ?? null }
      : null

  return { steps, requestResponse }
}

// Each step entry carries different "selected_*" convenience fields alongside its raw
// API response - pull out a small, presentable set of key/value pairs per step rather
// than dumping the full (often deeply nested) response.
function summarizeBookingData(step, entry) {
  const response = entry.response

  switch (step) {
    case "pos": {
      const pos = entry.pos_selected
      if (!pos) return {}
      return {
        "POS ID": pos.id,
        Office: pos.officeId,
        Currency: pos.currency,
        Supplier: pos.apiId,
      }
    }
    case "category": {
      const data = {}
      if (entry.selected_category?.code) data["Category"] = entry.selected_category.code
      if (entry.selected_fare?.fareCode?.code) data["Fare code"] = entry.selected_fare.fareCode.code
      return data
    }
    case "cabin": {
      const cabin = entry.selected_cabin
      if (!cabin) return {}
      const data = { Cabin: cabin.number }
      if (cabin.location) data["Location"] = cabin.location
      if (cabin.occupancy) data["Occupancy"] = `${cabin.occupancy.min ?? "-"}-${cabin.occupancy.max ?? "-"}`
      return data
    }
    case "cabin_hold": {
      const insurances = response?.insurances ?? []
      return insurances.length ? { Insurances: insurances.length } : {}
    }
    case "price": {
      const data = {}
      if (response?.prices?.length) data["Price lines"] = response.prices.length
      const scheduleCount = Object.values(response?.payment_schedules ?? {}).flat().length
      if (scheduleCount) data["Payment schedules"] = scheduleCount
      return data
    }
    case "tokenize_card": {
      const token = response?.token
      return token ? { Token: `${token.slice(0, 8)}…` } : {}
    }
    case "create_reservation": {
      const confirmationNumber = entry.confirmation_number
      return confirmationNumber ? { "Confirmation number": confirmationNumber } : {}
    }
    default:
      return {}
  }
}

// Collapse repeated per-chunk citations into unique { title, url } sources.
function dedupeSources(chunks = []) {
  const seen = new Set()
  const sources = []
  for (const chunk of chunks) {
    const title = chunk.title || "Untitled"
    const url = chunk.url || ""
    const key = `${title}|${url}`
    if (seen.has(key)) continue
    seen.add(key)
    sources.push({ title, url })
  }
  return sources
}

// A distinct assistant message representing a failed request.
export function makeErrorMessage(content) {
  return { id: uid(), role: "assistant", type: "error", content }
}
