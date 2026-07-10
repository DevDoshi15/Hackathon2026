import { Sparkles } from "lucide-react"

import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Skeleton } from "@/components/ui/skeleton"

// Shown while waiting for an assistant response. Mirrors the assistant bubble
// layout with shimmering skeleton lines.
export default function LoadingIndicator() {
  return (
    <div className="flex items-start gap-3">
      <Avatar className="mt-0.5 ring-1 ring-primary/30">
        <AvatarFallback className="bg-primary/15 text-primary">
          <Sparkles className="size-4" />
        </AvatarFallback>
      </Avatar>
      <div className="flex min-w-0 max-w-[85%] flex-col gap-2 rounded-2xl rounded-tl-sm border border-border/60 bg-card/60 px-4 py-3.5 backdrop-blur-sm">
        <Skeleton className="h-3 w-52 bg-primary/10" />
        <Skeleton className="h-3 w-64 bg-primary/10" />
        <Skeleton className="h-3 w-40 bg-primary/10" />
      </div>
    </div>
  )
}
