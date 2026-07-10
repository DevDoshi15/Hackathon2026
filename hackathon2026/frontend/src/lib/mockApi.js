// Mock response layer. Simulates the backend's /api/v1/booking responses so the
// chat UI can render all three assistant variants without wiring the real API.

export const uid = () =>
  Math.random().toString(36).slice(2, 10) + Date.now().toString(36)

// The assistant cycles through these response types on each send so every
// variant is easy to see.
const TYPES = ["text", "kb", "booking"]
let cursor = 0

export function makeAssistantMessage(type, prompt = "") {
  switch (type) {
    case "kb":
      return {
        id: uid(),
        role: "assistant",
        type: "kb",
        content:
          "For cruise bookings we support several **payment schedule types**:\n\n" +
          "- **Full payment** — charged immediately at confirmation.\n" +
          "- **Deposit + balance** — a deposit now, with the balance due before the sailing date.\n" +
          "- **Pay to supplier** — the cruise line collects the balance directly.\n\n" +
          "The available options depend on the sailing date and each cruise line's rules.",
        sources: [
          {
            title: "Payment schedule types",
            url: "https://kb.example.com/payment-schedule-types",
          },
          {
            title: "Nitro payment options",
            url: "https://kb.example.com/nitro-payment-options",
          },
          {
            title: "Pay to supplier",
            url: "https://kb.example.com/pay-to-supplier",
          },
        ],
      }
    case "booking":
      return {
        id: uid(),
        role: "assistant",
        type: "booking",
        booking: {
          step: "cabin",
          status: "success",
          message: "Cabin selected.",
          data: {
            Cabin: "9210",
            Location: "Port",
            Occupancy: "0-3",
          },
        },
      }
    case "text":
    default:
      return {
        id: uid(),
        role: "assistant",
        type: "text",
        content:
          "I can help you **plan and book a cruise** end to end — searching sailings, " +
          "choosing a cabin category, adding travellers, and handling payment.\n\n" +
          "Try asking things like:\n\n" +
          "1. *\"Create a booking for package P-10294 up to the cabin step\"*\n" +
          "2. *\"What payment options are supported?\"*\n\n" +
          "What would you like to do" +
          (prompt ? " next" : "") +
          "?",
      }
  }
}

// Resolves after ~1s with the next response variant in the cycle.
export function mockRespond(prompt) {
  const type = TYPES[cursor % TYPES.length]
  cursor += 1
  return new Promise((resolve) => {
    setTimeout(() => resolve(makeAssistantMessage(type, prompt)), 1000)
  })
}
