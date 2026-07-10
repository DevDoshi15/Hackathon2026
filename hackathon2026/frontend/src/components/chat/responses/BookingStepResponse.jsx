import { Fragment, useState } from "react"
import {
  AlertTriangle,
  BadgeCheck,
  BedDouble,
  Check,
  ChevronDown,
  CreditCard,
  HelpCircle,
  LayoutGrid,
  Lock,
  Package,
  Receipt,
} from "lucide-react"

import { Card } from "@/components/ui/card"
import { cn } from "@/lib/utils"

// The seven-step booking workflow, mirroring the backend's WORKFLOW_STEPS order:
// pos -> category -> cabin -> cabin_hold -> price -> tokenize_card -> create_reservation.
const STEPS = [
  { key: "pos", label: "POS", Icon: Package },
  { key: "category", label: "Category", Icon: LayoutGrid },
  { key: "cabin", label: "Cabin", Icon: BedDouble },
  { key: "cabin_hold", label: "Hold", Icon: Lock },
  { key: "price", label: "Price", Icon: Receipt },
  { key: "tokenize_card", label: "Payment", Icon: CreditCard },
  { key: "create_reservation", label: "Confirm", Icon: BadgeCheck },
]

function stepLabel(key) {
  return STEPS.find((item) => item.key === key)?.label ?? prettyKey(key)
}

function prettyKey(key) {
  return key.replace(/_/g, " ")
}

// A card showing a progress bar across all seven steps, plus one summary box per
// step actually executed so far (booking.steps), in order. Only the last step (the
// one the flow stopped at) gets a "Request / Response" detail toggle - earlier
// steps only show their summary.
export default function BookingStepResponse({ booking }) {
  const { steps = [] } = booking
  const last = steps[steps.length - 1]
  const currentIndex = Math.max(
    0,
    STEPS.findIndex((item) => item.key === last?.step)
  )

  return (
    <Card className="gap-0 overflow-hidden rounded-2xl rounded-tl-sm border-border/60 bg-card/70 py-0 shadow-sm backdrop-blur-sm">
      {/* Header */}
      <div className="flex items-center gap-2 border-b border-border/60 px-4 py-3">
        <span className="text-xs font-medium uppercase tracking-wider text-primary">
          Booking workflow
        </span>
        <span className="ml-auto rounded-full bg-primary/15 px-2 py-0.5 text-[11px] font-medium text-primary">
          Step {currentIndex + 1} of {STEPS.length}
        </span>
      </div>

      {/* Progress indicator */}
      <div className="flex items-center px-5 pb-7 pt-4">
        {STEPS.map((item, index) => {
          const done = index < currentIndex
          const current = index === currentIndex
          const currentFailed = current && last?.status === "failed"
          const currentNeedsInput = current && last?.status === "needs_input"
          const Icon = item.Icon

          return (
            <Fragment key={item.key}>
              {index > 0 && (
                <div
                  className={cn(
                    "h-0.5 flex-1 rounded-full transition-colors",
                    index <= currentIndex ? "bg-primary" : "bg-border"
                  )}
                />
              )}
              <div className="relative flex flex-col items-center">
                <div
                  className={cn(
                    "flex size-8 items-center justify-center rounded-full border transition-all",
                    done && "border-primary bg-primary text-primary-foreground",
                    current &&
                      !currentFailed &&
                      !currentNeedsInput &&
                      "border-primary bg-primary/15 text-primary shadow-[0_0_0_4px] shadow-primary/15",
                    currentFailed &&
                      "border-destructive bg-destructive/15 text-destructive shadow-[0_0_0_4px] shadow-destructive/15",
                    currentNeedsInput &&
                      "border-amber-500 bg-amber-500/15 text-amber-600 shadow-[0_0_0_4px] shadow-amber-500/15",
                    !done &&
                      !current &&
                      "border-border bg-secondary text-muted-foreground"
                  )}
                >
                  {done ? (
                    <Check className="size-4" />
                  ) : currentFailed ? (
                    <AlertTriangle className="size-4" />
                  ) : currentNeedsInput ? (
                    <HelpCircle className="size-4" />
                  ) : (
                    <Icon className="size-4" />
                  )}
                </div>
                <span
                  className={cn(
                    "absolute top-full mt-1.5 whitespace-nowrap text-[10px] font-medium",
                    current
                      ? "text-foreground"
                      : done
                        ? "text-muted-foreground"
                        : "text-muted-foreground/60"
                  )}
                >
                  {item.label}
                </span>
              </div>
            </Fragment>
          )
        })}
      </div>

      {/* One box per executed step */}
      {steps.length > 0 && (
        <div className="divide-y divide-border/60 border-t border-border/60">
          {steps.map((entry, index) => (
            <StepBox
              key={`${entry.step}-${index}`}
              entry={entry}
              requestResponse={booking.requestResponse}
              isLast={index === steps.length - 1}
            />
          ))}
        </div>
      )}
    </Card>
  )
}

function StepBox({ entry, requestResponse, isLast }) {
  const { step, status, message, data = {} } = entry
  const entries = Object.entries(data)
  const isFinal = step === "create_reservation" && status === "success"
  const showRequestResponse = isLast && (requestResponse?.request || requestResponse?.response)

  return (
    <div className="px-4 py-3">
      <div className="mb-1.5 flex items-center gap-2">
        <span className="text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">
          {stepLabel(step)}
        </span>
        <StatusBadge status={status} />
      </div>

      {message && (
        <p
          className={cn(
            "mb-2 text-sm",
            status === "failed"
              ? "text-destructive"
              : status === "needs_input"
                ? "text-amber-600"
                : "text-card-foreground"
          )}
        >
          {message}
        </p>
      )}

      {isFinal && data["Confirmation number"] && (
        <div className="mb-2 flex items-center justify-between rounded-lg bg-primary/10 px-3 py-2">
          <span className="text-xs font-medium uppercase tracking-wide text-primary">
            Confirmation number
          </span>
          <span className="text-sm font-semibold text-primary">
            {data["Confirmation number"]}
          </span>
        </div>
      )}

      {entries.length > 0 && (
        <dl className="grid grid-cols-1 gap-x-6 gap-y-1.5 sm:grid-cols-2">
          {entries
            .filter(([key]) => !(isFinal && key === "Confirmation number"))
            .map(([key, value]) => (
              <div
                key={key}
                className="flex items-baseline justify-between gap-3 border-b border-border/40 py-1 last:border-0"
              >
                <dt className="text-xs capitalize text-muted-foreground">{prettyKey(key)}</dt>
                <dd className="text-right text-xs font-medium text-foreground">{String(value)}</dd>
              </div>
            ))}
        </dl>
      )}

      {showRequestResponse && <RequestResponsePanel requestResponse={requestResponse} />}
    </div>
  )
}

function StatusBadge({ status }) {
  if (status === "failed") {
    return (
      <span className="rounded-full bg-destructive/15 px-1.5 py-0.5 text-[10px] font-medium text-destructive">
        Failed
      </span>
    )
  }
  if (status === "needs_input") {
    return (
      <span className="rounded-full bg-amber-500/15 px-1.5 py-0.5 text-[10px] font-medium text-amber-600">
        Needs input
      </span>
    )
  }
  return (
    <span className="rounded-full bg-primary/15 px-1.5 py-0.5 text-[10px] font-medium text-primary">
      Success
    </span>
  )
}

// Collapsible, side-by-side scrollable JSON view of the raw request sent and response
// received for the last executed step. Collapsed by default.
function RequestResponsePanel({ requestResponse }) {
  const [open, setOpen] = useState(false)
  const { request, response } = requestResponse

  return (
    <div className="mt-3 border-t border-border/60 pt-2">
      <button
        type="button"
        onClick={() => setOpen((value) => !value)}
        aria-expanded={open}
        className="flex w-full items-center gap-1.5 text-xs font-medium text-muted-foreground transition-colors hover:text-foreground"
      >
        Request / Response
        <ChevronDown className={cn("ml-auto size-3.5 transition-transform", open && "rotate-180")} />
      </button>

      {open && (
        <div className="mt-2 grid grid-cols-1 gap-2 sm:grid-cols-2">
          <JsonPane title="Request" value={request} />
          <JsonPane title="Response" value={response} />
        </div>
      )}
    </div>
  )
}

function JsonPane({ title, value }) {
  return (
    <div className="overflow-hidden rounded-lg border border-border/60 bg-secondary/40">
      <div className="border-b border-border/60 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-wide text-muted-foreground">
        {title}
      </div>
      <pre className="max-h-64 overflow-auto p-2.5 text-[11px] leading-relaxed text-foreground">
        {value ? JSON.stringify(value, null, 2) : "—"}
      </pre>
    </div>
  )
}
