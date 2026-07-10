import { useEffect, useRef, useState } from "react"

// Reveal speed in milliseconds per character. ~15-25ms reads as natural
// streaming; tune this single constant to taste.
export const TYPEWRITER_SPEED_MS = 5

// Reveals `text` one character at a time. Returns the visible slice, whether it
// is still streaming, and a `skip()` to jump straight to the full text.
//
// `onStreamingChange(bool)` fires on the start/complete transitions so a parent
// can react (e.g. pulse an avatar). It is held in a ref so passing a fresh
// inline callback each render never restarts the reveal animation.
export function useTypewriter(
  text = "",
  { speed = TYPEWRITER_SPEED_MS, enabled = true, onStreamingChange } = {}
) {
  const [count, setCount] = useState(enabled ? 0 : text.length)
  const intervalRef = useRef(null)
  const onStreamingChangeRef = useRef(onStreamingChange)

  // Keep the latest callback without retriggering the reveal effect below.
  useEffect(() => {
    onStreamingChangeRef.current = onStreamingChange
  }, [onStreamingChange])

  useEffect(() => {
    if (!enabled || !text) {
      setCount(text.length)
      return
    }

    setCount(0)
    intervalRef.current = setInterval(() => {
      setCount((previous) => {
        const next = previous + 1
        if (next >= text.length) {
          clearInterval(intervalRef.current)
          intervalRef.current = null
          return text.length
        }
        return next
      })
    }, speed)

    return () => {
      clearInterval(intervalRef.current)
      intervalRef.current = null
    }
  }, [text, speed, enabled])

  const isStreaming = count < text.length

  // Notify the parent on start/complete transitions only. isStreaming is a
  // boolean, so this effect skips the per-character re-renders in between.
  useEffect(() => {
    onStreamingChangeRef.current?.(isStreaming)
  }, [isStreaming])

  function skip() {
    clearInterval(intervalRef.current)
    intervalRef.current = null
    setCount(text.length)
  }

  return {
    displayed: text.slice(0, count),
    isStreaming,
    skip,
  }
}
