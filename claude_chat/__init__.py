"""Reusable helpers for talking to Claude from any lesson script.

Usage:
    from claude_chat import Conversation, create_client

    conversation = Conversation(create_client(), system="You are a patient math tutor.")
    print(conversation.ask("How do I solve 2x + 3 = 7?"))
"""

# Principle: DRY
# Why: every lesson imports these from one package instead of copy-pasting the same helpers into each main.py.
from claude_chat.client import DEFAULT_MAX_TOKENS, DEFAULT_MODEL, create_client
from claude_chat.conversation import Conversation

__all__ = ["Conversation", "create_client", "DEFAULT_MODEL", "DEFAULT_MAX_TOKENS"]
