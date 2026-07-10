import { useMemo, useRef } from "react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"

import { cn } from "@/lib/utils"
import { useTypewriter } from "@/hooks/useTypewriter"
import ScrollableBubble from "../ScrollableBubble"
import CopyButton from "../CopyButton"
import { createMarkdownComponents } from "../markdownComponents"

// Simple markdown-rendered assistant text, in a glassy bubble. Streams in
// character-by-character; click the bubble to skip the animation. Caps height
// and scrolls internally for long answers. Copy buttons (message + per code
// block) appear on hover once streaming completes.
export default function PlainTextResponse({ content, onStreamingChange }) {
  const { displayed, isStreaming, skip } = useTypewriter(content, {
    onStreamingChange,
  })
  const mdRef = useRef(null)
  const components = useMemo(
    () => createMarkdownComponents({ showCodeCopy: !isStreaming }),
    [isStreaming]
  )

  return (
    <ScrollableBubble
      onClick={isStreaming ? skip : undefined}
      title={isStreaming ? "Click to skip" : undefined}
      className={cn(
        "rounded-2xl rounded-tl-sm border border-border/60 bg-card/60 text-card-foreground shadow-sm backdrop-blur-sm",
        isStreaming && "cursor-pointer"
      )}
      innerClassName="px-4 py-3"
      fadeClassName="from-card"
    >
      <div ref={mdRef} className={cn("md", isStreaming && "is-streaming")}>
        <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
          {displayed}
        </ReactMarkdown>
      </div>

      {!isStreaming && (
        <div className="mt-2 flex justify-end opacity-0 transition-opacity focus-within:opacity-100 group-hover:opacity-100">
          <CopyButton withText getText={() => mdRef.current?.innerText ?? ""} />
        </div>
      )}
    </ScrollableBubble>
  )
}
