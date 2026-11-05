"""Lesson: prompt evaluation — run one prompt template against a small dataset of tasks."""

from anthropic import Anthropic

from claude_chat import Conversation, create_client

DATASET = [
    {"task": "Create a Python function to extract the AWS account ID from an ARN"},
    {"task": "Write a JSON policy document that allows read-only access to a specific S3 bucket"},
]


# Clean Code: Small Functions
# Why: the template needs a task to fill in, so it is a function instead of an f-string that ran before `task` existed.
def build_prompt(task: str) -> str:
    return f"""
Please provide a solution to the following task:
{task}
"""


def run_prompt(client: Anthropic, task: str) -> str:
    """Ask Claude to solve one task in a fresh conversation and return the reply."""
    return Conversation(client).ask(build_prompt(task))


# Pattern: Dependency Injection
# Why: one client is created here and passed to every run_prompt call instead of each call building its own.
def main() -> None:
    client = create_client()
    for test_case in DATASET:
        print(run_prompt(client, test_case["task"]))


if __name__ == "__main__":
    main()
