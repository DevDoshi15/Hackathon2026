import { Anchor } from "lucide-react"

import ChatInput from "./ChatInput"
import MessageList from "./MessageList"

// The overall chat shell. Two states:
//  - Empty (no messages yet): centered welcome + centered input.
//  - Active: scrollable message list with the input pinned to the bottom.
// The header is shown in both states.
export default function ChatLayout({ messages, isLoading, onSend }) {
  const isEmpty = messages.length === 0

  return (
    <div className="relative flex h-svh flex-col overflow-hidden bg-background text-foreground">
      {/* Ambient accent glow */}
      <div
        aria-hidden
        className="pointer-events-none absolute inset-x-0 -top-48 z-0 mx-auto h-96 max-w-3xl rounded-full bg-primary/15 blur-[130px]"
      />

      {/* Header */}
      <header className="relative z-10 flex h-14 shrink-0 items-center gap-3 border-b border-border/60 bg-background/70 px-4 backdrop-blur-xl sm:px-6">
        <div className="flex size-8 items-center justify-center rounded-lg bg-primary/15 ring-1 ring-primary/30">
          <Anchor className="size-4 text-primary" />
        </div>
        <div className="flex flex-col leading-none">
          <span className="text-sm font-semibold tracking-tight">VOYAGER</span>
          <span className="text-[11px] text-muted-foreground">
            AI Travel Agent
          </span>
        </div>
        <div className="ml-auto flex items-center gap-1.5 text-[11px] text-muted-foreground">
          <span className="size-1.5 rounded-full bg-primary shadow-[0_0_8px] shadow-primary" />
          Online
        </div>
      </header>

      {isEmpty ? (
        /* Empty state: centered welcome with the input directly below */
        <div className="relative z-10 flex flex-1 flex-col items-center justify-center px-4 pb-16">
          <div className="w-full max-w-2xl text-center">
            <h1 className="text-3xl font-semibold tracking-tight sm:text-4xl">
              Hey there, I&apos;m{" "}
              <span className="text-primary">VOYAGER</span>
            </h1>
            <p className="mt-3 text-base text-muted-foreground">
              Your compass through the booking API
            </p>
            <div className="mt-8">
              <ChatInput isLoading={isLoading} onSend={onSend} />
            </div>
          </div>
        </div>
      ) : (
        /* Active chat: message list + bottom-pinned input */
        <>
          <MessageList messages={messages} isLoading={isLoading} />
          <div className="relative z-10 shrink-0 border-t border-border/60 bg-background/70 px-4 py-3 backdrop-blur-xl sm:px-6">
            <div className="mx-auto max-w-3xl">
              <ChatInput isLoading={isLoading} onSend={onSend} />
            </div>
            <p className="mx-auto mt-1.5 max-w-3xl text-center text-[10px] text-muted-foreground/70">
              VOYAGER can make mistakes. Responses shown here are simulated.
            </p>
          </div>
        </>
      )}
    </div>
  )
}
