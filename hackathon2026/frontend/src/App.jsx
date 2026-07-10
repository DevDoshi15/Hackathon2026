import { useState } from "react"

import ChatLayout from "@/components/chat/ChatLayout"
import { mockRespond, uid } from "@/lib/mockApi"
import { API_BASE_URL, USE_MOCK, makeErrorMessage, sendPrompt } from "@/lib/api"

export default function App() {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  async function handleSend(prompt) {
    const userMessage = {
      id: uid(),
      role: "user",
      type: "text",
      content: prompt,
    }
    setMessages((previous) => [...previous, userMessage])
    setIsLoading(true)

    try {
      // USE_MOCK swaps back to the built-in mock responses (mockApi.js).
      const reply = USE_MOCK
        ? await mockRespond(prompt)
        : await sendPrompt(prompt)
      setMessages((previous) => [...previous, reply])
    } catch (error) {
      // Keep the app alive and the input usable; show a distinct error bubble.
      setMessages((previous) => [
        ...previous,
        makeErrorMessage(
          `I couldn't reach the booking API at ${API_BASE_URL}. ` +
            `Make sure the backend is running, then try again. (${error.message})`
        ),
      ])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <ChatLayout messages={messages} isLoading={isLoading} onSend={handleSend} />
  )
}
