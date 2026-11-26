"""Lesson: get clean JSON from Claude with an assistant prefill and a stop sequence."""

import json

from claude_chat import add_assistant_message, add_user_message, chat

messages = []
add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])

event_rule = json.loads(text.strip())
print(json.dumps(event_rule, indent=2))
