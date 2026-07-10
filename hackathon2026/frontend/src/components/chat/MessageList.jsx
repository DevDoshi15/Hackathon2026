import { useEffect, useRef } from "react"

import UserMessage from "./UserMessage"
import AssistantMessage from "./AssistantMessage"
import LoadingIndicator from "./LoadingIndicator"

// How close to the bottom (px) still counts as "following" the conversation.
const NEAR_BOTTOM_PX = 120

// Scrollable middle region. Sticks to the bottom as content grows — including
// while an assistant message streams in — but only when the user is already
// near the bottom, so scrolling up to read history is never yanked away.
export default function MessageList({ messages, isLoading }) {
  const scrollRef = useRef(null)
  const contentRef = useRef(null)
  // Whether we should keep pinning to the bottom. Updated as the user scrolls.
  const stickRef = useRef(true)

  function scrollToBottom() {
    const scroller = scrollRef.current
    if (scroller) scroller.scrollTop = scroller.scrollHeight
  }

  function handleScroll() {
    const scroller = scrollRef.current
    if (!scroller) return
    const distanceFromBottom =
      scroller.scrollHeight - scroller.scrollTop - scroller.clientHeight
    stickRef.current = distanceFromBottom <= NEAR_BOTTOM_PX
  }

  // A new message (or the loading indicator) re-engages sticking and jumps down.
  useEffect(() => {
    stickRef.current = true
    scrollToBottom()
  }, [messages, isLoading])

  // Follow content height changes (streaming text, expanding sources, wrapping)
  // and keep pinned to the bottom while the user is following along.
  useEffect(() => {
    const content = contentRef.current
    if (!content) return
    const observer = new ResizeObserver(() => {
      if (stickRef.current) scrollToBottom()
    })
    observer.observe(content)
    return () => observer.disconnect()
  }, [])

  return (
    <div
      ref={scrollRef}
      onScroll={handleScroll}
      className="scrollbar-thin relative z-10 flex-1 overflow-y-auto"
    >
      <div
        ref={contentRef}
        className="mx-auto flex max-w-3xl flex-col gap-5 px-4 py-6 sm:px-6"
      >
        {messages.map((message) =>
          message.role === "user" ? (
            <UserMessage key={message.id} message={message} />
          ) : (
            <AssistantMessage key={message.id} message={message} />
          )
        )}
        {isLoading && <LoadingIndicator />}
      </div>
    </div>
  )
}
