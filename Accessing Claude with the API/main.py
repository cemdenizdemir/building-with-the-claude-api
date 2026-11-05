"""Lesson: get clean JSON from Claude with an assistant prefill and a stop sequence."""

import json

from claude_chat import Conversation, create_client


# Clean Code: Entry-Point Guard
# Why: the API call runs only when this file is executed, not when another file imports it.
def main() -> None:
    conversation = Conversation(create_client())
    conversation.add_user_message("Generate a very short event bridge rule as json")

    # Prefill the reply with an opening fence so Claude writes only JSON, then stop at the closing fence.
    conversation.add_assistant_message("```json")
    text = conversation.send(stop_sequences=["```"])

    event_rule = json.loads(text.strip())
    print('event_rule["Name"] =', event_rule["Name"])
    conversation.add_assistant_message(text)  # or "```json" + text for the full turn

    print(conversation.format_history())


if __name__ == "__main__":
    main()
