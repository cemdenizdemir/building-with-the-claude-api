from dotenv import load_dotenv
load_dotenv()

import json

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step. Finish your answer with abc123
"""

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    return message.content[0].text

def print_history(messages):
    print("\n--- Conversation History ---")
    for message in messages:
        role = message["role"].capitalize()
        print(f"\n{role}:\n{message['content']}")
        print("-" * 40)

messages = []

# add_user_message(messages, "Write a 1 sentence description of a fake database")
# # answer = chat(messages, system=system_prompt)
# with client.messages.stream(
#     model=model,
#     max_tokens=1000,
#     messages=messages,
# ) as stream:
#     for text in stream.text_stream:
#         # print(text, end="")
#         pass

#     final_message = stream.get_final_message()

# add_assistant_message(messages, answer)
# print("ai with system prompt response:", answer)

# add_assistant_message(messages, final_message.content[0].text)
# print("ai with system prompt response:", final_message.content[0].text)

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])

clean_json = json.loads(text.strip())
print("clean_json[\"Name\"] = ", clean_json["Name"])  
add_assistant_message(messages, text)  # or "```json" + text for the full turn

print_history(messages)





# -------------------------------------------------------

# import os
# import re
# import sys

# import anthropic
# from dotenv import load_dotenv

# KEY_PATTERN = re.compile(r"^sk-ant-[A-Za-z0-9_\-]{20,}$")
# PLACEHOLDERS = {"your-api-key-here", "changeme", "xxx"}


# def load_api_key() -> str:
#     """Load ANTHROPIC_API_KEY from .env / environment and validate its format."""
#     load_dotenv()
#     key = os.getenv("ANTHROPIC_API_KEY", "").strip()

#     if not key:
#         sys.exit("Error: ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")
#     if key.lower() in PLACEHOLDERS or "your" in key.lower():
#         sys.exit("Error: ANTHROPIC_API_KEY is still a placeholder value.")
#     if not KEY_PATTERN.match(key):
#         sys.exit("Error: ANTHROPIC_API_KEY has an invalid format (expected 'sk-ant-...', no spaces or quotes).")
#     return key


# def main() -> None:
#     client = anthropic.Anthropic(api_key=load_api_key())
#     try:
#         message = client.messages.create(
#             model="claude-haiku-4-5",
#             max_tokens=1024,
#             messages=[{"role": "user", "content": "Hello, world"}],
#         )
#     except anthropic.AuthenticationError:
#         sys.exit("Error: the API key was rejected. Check that it is valid and not revoked.")
#     except anthropic.APIError as e:
#         sys.exit(f"API error: {e}")
#     print(message.content)


# if __name__ == "__main__":
#     main()
