import { useMemo, useRef, useState } from "react"
import { BookOpen, ChevronDown, ExternalLink } from "lucide-react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"

import { cn } from "@/lib/utils"
import { useTypewriter } from "@/hooks/useTypewriter"
import ScrollableBubble from "../ScrollableBubble"
import CopyButton from "../CopyButton"
import { createMarkdownComponents } from "../markdownComponents"

// Markdown answer plus a collapsible "Sources" section listing citation titles.
// The answer streams in; sources appear once streaming completes. Click the
// bubble while streaming to skip the animation. Caps height and scrolls
// internally (answer + sources) for long answers. Copy buttons (answer + per
// code block) appear on hover once streaming completes; the message copy copies
// the answer text only (not the sources).
export default function KBAnswerResponse({ content, sources = [], onStreamingChange }) {
  const [open, setOpen] = useState(false)
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
        <div className="mt-3 flex justify-end opacity-0 transition-opacity focus-within:opacity-100 group-hover:opacity-100">
          <CopyButton withText getText={() => mdRef.current?.innerText ?? ""} />
        </div>
      )}

      {!isStreaming && sources.length > 0 && (
        <div className="mt-3 border-t border-border/60 pt-2">
          <button
            type="button"
            onClick={() => setOpen((value) => !value)}
            aria-expanded={open}
            className="flex w-full items-center gap-1.5 text-xs font-medium text-muted-foreground transition-colors hover:text-foreground"
          >
            <BookOpen className="size-3.5 text-primary" />
            {sources.length} source{sources.length > 1 ? "s" : ""}
            <ChevronDown
              className={cn(
                "ml-auto size-3.5 transition-transform",
                open && "rotate-180"
              )}
            />
          </button>

          {open && (
            <ul className="mt-2 space-y-1">
              {sources.map((source, index) => (
                <li key={`${source.title}-${index}`}>
                  <a
                    href={source.url || "#"}
                    target="_blank"
                    rel="noreferrer"
                    className="group flex items-center gap-2 rounded-md px-2 py-1.5 text-xs text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
                  >
                    <span className="flex size-4 shrink-0 items-center justify-center rounded bg-primary/15 text-[10px] font-semibold text-primary">
                      {index + 1}
                    </span>
                    <span className="truncate">{source.title}</span>
                    <ExternalLink className="ml-auto size-3 shrink-0 opacity-0 transition-opacity group-hover:opacity-100" />
                  </a>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </ScrollableBubble>
  )
}
