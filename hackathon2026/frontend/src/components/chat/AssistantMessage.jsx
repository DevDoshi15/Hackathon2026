import { useState } from "react"
import { Sparkles } from "lucide-react"

import { cn } from "@/lib/utils"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import PlainTextResponse from "./responses/PlainTextResponse"
import KBAnswerResponse from "./responses/KBAnswerResponse"
import BookingStepResponse from "./responses/BookingStepResponse"
import ErrorResponse from "./responses/ErrorResponse"

// Left-aligned assistant message. Picks a response sub-component based on the
// message `type` field ('text' | 'kb' | 'booking'). Streaming state is lifted
// here from the streaming child (via onStreamingChange) so the avatar can pulse
// while text is being revealed. Booking responses render instantly and never
// report streaming, so the avatar stays static for them.
function renderBody(message, onStreamingChange) {
  switch (message.type) {
    case "kb":
      return (
        <KBAnswerResponse
          content={message.content}
          sources={message.sources}
          onStreamingChange={onStreamingChange}
        />
      )
    case "booking":
      return <BookingStepResponse booking={message.booking} />
    case "error":
      return <ErrorResponse content={message.content} />
    case "text":
    default:
      return (
        <PlainTextResponse
          content={message.content}
          onStreamingChange={onStreamingChange}
        />
      )
  }
}

export default function AssistantMessage({ message }) {
  const [isStreaming, setIsStreaming] = useState(false)

  return (
    <div className="flex items-start gap-3">
      <Avatar
        className={cn(
          "mt-0.5 ring-1 transition-shadow",
          isStreaming
            ? "shadow-[0_0_12px] shadow-primary/30 ring-primary/60"
            : "ring-primary/30"
        )}
      >
        <AvatarFallback className="bg-primary/15 text-primary">
          <Sparkles
            className={cn("size-4", isStreaming && "animate-avatar-breathe")}
          />
        </AvatarFallback>
      </Avatar>
      <div className="min-w-0 max-w-[85%]">
        {renderBody(message, setIsStreaming)}
      </div>
    </div>
  )
}
