import { Fragment } from "react"
import {
  AlertTriangle,
  BadgeCheck,
  BedDouble,
  Check,
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
// package -> category -> cabin -> cabin_hold -> price -> tokenize_card -> create_reservation.
const STEPS = [
  { key: "package", label: "Package", Icon: Package },
  { key: "category", label: "Category", Icon: LayoutGrid },
  { key: "cabin", label: "Cabin", Icon: BedDouble },
  { key: "cabin_hold", label: "Hold", Icon: Lock },
  { key: "price", label: "Price", Icon: Receipt },
  { key: "tokenize_card", label: "Payment", Icon: CreditCard },
  { key: "create_reservation", label: "Confirm", Icon: BadgeCheck },
]

function prettyKey(key) {
  return key.replace(/_/g, " ")
}

// A card showing the current step, a visual progress indicator across all seven
// steps, a status-aware message, and the step's data as key-value pairs.
// `booking.status` is one of "success" | "failed" | "needs_input" (set by
// mapBookingPayload in api.js) - failed/needs_input tint the current step red/amber
// instead of the default primary color.
export default function BookingStepResponse({ booking }) {
  const { step, status = "success", message, data = {} } = booking
  const currentIndex = Math.max(
    0,
    STEPS.findIndex((item) => item.key === step)
  )
  const entries = Object.entries(data)
  const isFinal = step === "create_reservation" && status === "success"

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
          const currentFailed = current && status === "failed"
          const currentNeedsInput = current && status === "needs_input"
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

      {/* Step data */}
      {(message || entries.length > 0) && (
        <div className="border-t border-border/60 px-4 py-3">
          {message && (
            <p
              className={cn(
                "mb-2.5 text-sm",
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
            <div className="mb-2.5 flex items-center justify-between rounded-lg bg-primary/10 px-3 py-2">
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
                    <dt className="text-xs capitalize text-muted-foreground">
                      {prettyKey(key)}
                    </dt>
                    <dd className="text-right text-xs font-medium text-foreground">
                      {String(value)}
                    </dd>
                  </div>
                ))}
            </dl>
          )}
        </div>
      )}
    </Card>
  )
}
