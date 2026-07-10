import { useState } from "react"
import { Send } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

// The prompt input + send button. Owns its own draft value and is reused by
// both the empty-state welcome and the pinned bottom bar.
export default function ChatInput({ isLoading, onSend, autoFocus = true }) {
  const [value, setValue] = useState("")
  const canSend = value.trim().length > 0 && !isLoading

  function handleSubmit(event) {
    event.preventDefault()
    if (!canSend) return
    onSend(value.trim())
    setValue("")
  }

  return (
    <form onSubmit={handleSubmit} className="flex w-full items-center gap-2">
      <Input
        value={value}
        onChange={(event) => setValue(event.target.value)}
        placeholder={
          isLoading
            ? "Waiting for response…"
            : "Ask about a booking or anything travel…"
        }
        disabled={isLoading}
        autoFocus={autoFocus}
        className="h-11 flex-1 rounded-xl border-border/60 bg-card/60 px-4 text-sm shadow-sm backdrop-blur-sm md:text-sm"
      />
      <Button
        type="submit"
        size="icon"
        disabled={!canSend}
        aria-label="Send message"
        className="size-11 shrink-0 rounded-xl shadow-sm shadow-primary/20"
      >
        <Send className="size-4" />
      </Button>
    </form>
  )
}
