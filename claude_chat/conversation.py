"""A multi-turn conversation with Claude that owns its message history."""

from typing import Any

from anthropic import Anthropic
from anthropic.types import Message as ClaudeResponse

from claude_chat.client import DEFAULT_MAX_TOKENS, DEFAULT_MODEL

# Clean Code: Meaningful Names
# Why: the SDK already has a `Message` type (Claude's response), so the history entry gets its own name to avoid confusing the two.
ChatMessage = dict[str, str]


# OOP: Encapsulation
# Pattern: Facade
# Why: the message list and the SDK request details sit behind a few methods, so scripts can't corrupt the history or rebuild request dicts by hand.
class Conversation:
    """Keeps the message history and sends it to Claude."""

    # SOLID: Dependency Inversion (DIP)
    # Why: the client is passed in instead of created here, so a test can hand in a fake client and no real API call is made.
    def __init__(
        self,
        client: Anthropic,
        *,
        system: str | None = None,
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
    ) -> None:
        self._client = client
        self.system = system
        self.model = model
        self.max_tokens = max_tokens
        self._messages: list[ChatMessage] = []

    # Clean Code: Immutability
    # Why: callers get a copy, so the history can only change through the add_* methods.
    @property
    def messages(self) -> list[ChatMessage]:
        return [dict(message) for message in self._messages]

    def add_user_message(self, text: str) -> None:
        self._messages.append({"role": "user", "content": text})

    def add_assistant_message(self, text: str) -> None:
        """Store a reply, or prefill the start of the next one before calling send()."""
        self._messages.append({"role": "assistant", "content": text})

    def send(self, *, stop_sequences: list[str] | None = None) -> str:
        """Send the current history and return Claude's reply text without storing it."""
        params: dict[str, Any] = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": self._messages,
        }
        if self.system:
            params["system"] = self.system
        if stop_sequences:
            params["stop_sequences"] = stop_sequences

        response = self._client.messages.create(**params)
        return _extract_text(response)

    def ask(self, text: str, *, stop_sequences: list[str] | None = None) -> str:
        """Add a user message, send it, store the reply in the history and return it."""
        self.add_user_message(text)
        reply = self.send(stop_sequences=stop_sequences)
        self.add_assistant_message(reply)
        return reply

    # Principle: Separation of Concerns
    # Why: it returns a string instead of printing, so the caller decides where the history goes (console, file, log).
    def format_history(self) -> str:
        lines = ["", "--- Conversation History ---"]
        for message in self._messages:
            lines.append(f"\n{message['role'].capitalize()}:\n{message['content']}")
            lines.append("-" * 40)
        return "\n".join(lines)


# Clean Code: Explicit Error Handling
# Why: a reply can contain non-text blocks (e.g. tool use), so text blocks are joined instead of assuming content[0] is text.
def _extract_text(response: ClaudeResponse) -> str:
    return "".join(block.text for block in response.content if block.type == "text")
