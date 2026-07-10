import { useRef } from "react"

import CopyButton from "./CopyButton"

// Wraps react-markdown's <pre> (block code) with a copy button in the top-right
// corner. The button copies the block's text via the rendered pre's innerText,
// so it never includes the button itself or markdown fences.
function MarkdownCodeBlock({ node, showCopy = true, children, ...props }) {
  const preRef = useRef(null)
  return (
    <div className="group/code relative">
      <pre ref={preRef} {...props}>
        {children}
      </pre>
      {showCopy && (
        <CopyButton
          getText={() => preRef.current?.innerText ?? ""}
          className="absolute right-2 top-2 opacity-0 transition-opacity focus-visible:opacity-100 group-hover/code:opacity-100"
        />
      )}
    </div>
  )
}

// Builds the `components` map for ReactMarkdown. Code-block copy buttons are
// hidden until streaming completes (showCodeCopy=false during streaming).
export function createMarkdownComponents({ showCodeCopy = true } = {}) {
  return {
    pre: (props) => <MarkdownCodeBlock {...props} showCopy={showCodeCopy} />,
  }
}
