# %%
import os
import random
import re
import sys
from functools import partial
from pathlib import Path
from pprint import pprint
from typing import Any, Literal

from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI

import tests.test as tests

MAIN = __name__ == "__main__"

load_dotenv()

assert os.getenv("OPENAI_API_KEY") is not None, (
    "You must set your OpenAI API key - see instructions in dropdown"
)
assert os.getenv("ANTHROPIC_API_KEY") is not None, (
    "You must set your Anthropic API key - see instructions in dropdown"
)

# OPENAI_API_KEY

openai_client = OpenAI()
anthropic_client = Anthropic()

# %%
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a Haiku about a program that says hello world",
        },
    ],
    n=2,
)

# pprint(
#     response.model_dump()
# )  # See the entire ChatCompletion object, as a dict (more readable)
print("\n", response.choices[0].message.content)  # See the response message only

# %%
