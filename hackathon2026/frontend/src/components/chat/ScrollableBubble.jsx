import { useCallback, useEffect, useRef, useState } from "react"

import { cn } from "@/lib/utils"

// A message bubble that caps its height and scrolls internally once content
// overflows. Shows a bottom fade only while there is more content below (i.e.
// scrollable and not scrolled to the bottom). Never auto-scrolls — it stays
// wherever the user left it (top by default), even while content streams in.
//
// - className:      outer bubble styling (bg, border, rounding, shadow, blur)
// - innerClassName: padding/typography for the scroll area
// - fadeClassName:  gradient start color for the fade (e.g. "from-card")
// - maxHeightClassName: height cap (default max-h-[60vh])
export default function ScrollableBubble({
  className,
  innerClassName,
  fadeClassName,
  maxHeightClassName = "max-h-[60vh]",
  children,
  ...props
}) {
  const scrollRef = useRef(null)
  const contentRef = useRef(null)
  const [showFade, setShowFade] = useState(false)

  const update = useCallback(() => {
    const element = scrollRef.current
    if (!element) return
    const distanceFromBottom =
      element.scrollHeight - element.scrollTop - element.clientHeight
    setShowFade(distanceFromBottom > 8)
  }, [])

  useEffect(() => {
    update()
    const observer = new ResizeObserver(update)
    // Observe the scroll box (viewport height changes the vh-based cap) and the
    // content (grows during streaming, even after the box hits its cap).
    if (scrollRef.current) observer.observe(scrollRef.current)
    if (contentRef.current) observer.observe(contentRef.current)
    return () => observer.disconnect()
  }, [update])

  return (
    <div className={cn("group relative overflow-hidden", className)} {...props}>
      <div
        ref={scrollRef}
        onScroll={update}
        className={cn(
          "scrollbar-thin overflow-y-auto",
          maxHeightClassName,
          innerClassName
        )}
      >
        <div ref={contentRef}>{children}</div>
      </div>
      {showFade && (
        <div
          aria-hidden
          className={cn(
            "pointer-events-none absolute inset-x-0 bottom-0 h-10 bg-gradient-to-t to-transparent",
            fadeClassName
          )}
        />
      )}
    </div>
  )
}
