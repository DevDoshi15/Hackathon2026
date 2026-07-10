import { User } from "lucide-react"

import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import ScrollableBubble from "./ScrollableBubble"

// Right-aligned bubble for user prompts (plain text). Caps height and scrolls
// internally when a prompt is very long.
export default function UserMessage({ message }) {
  return (
    <div className="flex items-start justify-end gap-3">
      <ScrollableBubble
        className="max-w-[80%] rounded-2xl rounded-tr-sm bg-primary text-primary-foreground shadow-sm shadow-primary/20"
        innerClassName="whitespace-pre-wrap px-4 py-2.5 text-sm leading-relaxed"
        fadeClassName="from-primary"
      >
        {message.content}
      </ScrollableBubble>
      <Avatar className="mt-0.5 ring-1 ring-border">
        <AvatarFallback className="bg-secondary text-foreground">
          <User className="size-4" />
        </AvatarFallback>
      </Avatar>
    </div>
  )
}
