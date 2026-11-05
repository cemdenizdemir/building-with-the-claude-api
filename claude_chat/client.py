"""Client creation and shared defaults for every lesson script."""

from anthropic import Anthropic
from dotenv import load_dotenv

# Clean Code: Named Constants
# Why: the model id and token limit live in one place, so switching models is a one-line change for every script.
DEFAULT_MODEL = "claude-haiku-4-5"
DEFAULT_MAX_TOKENS = 1000


# Pattern: Factory
# Clean Code: No Import-Time Side Effects
# Why: .env loading and client setup run only when a script asks for a client, not whenever this package is imported.
def create_client() -> Anthropic:
    """Load ANTHROPIC_API_KEY from the nearest .env file and return a ready-to-use client."""
    load_dotenv()
    return Anthropic()
