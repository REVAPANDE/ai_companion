from __future__ import annotations

import os
from typing import Protocol


class ChatClient(Protocol):
    def complete(self, messages: list[dict[str, str]], model: str | None = None) -> str:
        ...


class GroqChatClient:
    def __init__(self) -> None:
        from groq import Groq

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not configured")
        self.client = Groq(api_key=api_key)
        self.default_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    def complete(self, messages: list[dict[str, str]], model: str | None = None) -> str:
        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=float(os.getenv("LLM_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("LLM_MAX_TOKENS", "1200")),
        )
        return response.choices[0].message.content or ""


def get_chat_client(provider: str = "groq") -> ChatClient:
    if provider != "groq":
        raise ValueError(f"Unsupported provider: {provider}")
    return GroqChatClient()
