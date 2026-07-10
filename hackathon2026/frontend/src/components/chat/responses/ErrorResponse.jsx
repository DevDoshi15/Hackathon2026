import { AlertTriangle } from "lucide-react"

// Distinct error-state bubble shown when a request to the backend fails.
export default function ErrorResponse({ content }) {
  return (
    <div className="flex items-start gap-2 rounded-2xl rounded-tl-sm border border-destructive/40 bg-destructive/10 px-4 py-3 text-sm leading-relaxed text-card-foreground shadow-sm backdrop-blur-sm">
      <AlertTriangle className="mt-0.5 size-4 shrink-0 text-destructive" />
      <span>{content}</span>
    </div>
  )
}
