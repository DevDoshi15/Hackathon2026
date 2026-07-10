import { useCallback, useEffect, useRef, useState } from "react"
import { Check, Copy } from "lucide-react"

import { cn } from "@/lib/utils"

async function writeClipboard(text) {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text)
      return true
    }
  } catch {
    // fall through to the legacy path below
  }
  try {
    const textarea = document.createElement("textarea")
    textarea.value = text
    textarea.style.position = "fixed"
    textarea.style.opacity = "0"
    document.body.appendChild(textarea)
    textarea.select()
    document.execCommand("copy")
    document.body.removeChild(textarea)
    return true
  } catch {
    return false
  }
}

// Small, subtle copy button. `getText` is called lazily on click so it always
// copies the current content. `withText` shows a "Copy"/"Copied!" label.
export default function CopyButton({ getText, className, withText = false }) {
  const [copied, setCopied] = useState(false)
  const timerRef = useRef(null)

  useEffect(() => () => clearTimeout(timerRef.current), [])

  const handleCopy = useCallback(
    async (event) => {
      event.stopPropagation() // don't trigger bubble click-to-skip
      const text = (typeof getText === "function" ? getText() : getText) || ""
      if (!text) return
      const ok = await writeClipboard(text)
      if (!ok) return
      setCopied(true)
      clearTimeout(timerRef.current)
      timerRef.current = setTimeout(() => setCopied(false), 1500)
    },
    [getText]
  )

  return (
    <button
      type="button"
      onClick={handleCopy}
      aria-label={copied ? "Copied" : "Copy"}
      title={copied ? "Copied!" : "Copy"}
      className={cn(
        "inline-flex items-center gap-1 rounded-md border border-border/60 bg-card/70 px-1.5 py-1 text-muted-foreground backdrop-blur-sm transition-colors hover:border-primary/40 hover:text-primary",
        className
      )}
    >
      {copied ? (
        <Check className="size-3.5 text-primary" />
      ) : (
        <Copy className="size-3.5" />
      )}
      {withText && (
        <span className="text-[11px] font-medium">
          {copied ? "Copied!" : "Copy"}
        </span>
      )}
    </button>
  )
}
