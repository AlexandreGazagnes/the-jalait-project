"""
Prediction Module
"""

import os
import logging
import time

from openai import OpenAI

client = OpenAI()
import pandas as pd

from jalait.prompts import prompts
from .prompts._base import BasePrompt


from jalait.env import manage_env


def completion_from_messages(
    messages: list[dict] | BasePrompt,
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.0,
    api_key: str = None,
):
    """make a completion request to openai

    Positional arguments:
        - messages : list | BasePrompt : messages to send to openai
        - api_key : str : openai api key

    Positional arguments:
        - model : str : openai model
        - temperature : float : openai temperature between 0 and 1"""

    api_key = api_key if api_key else os.getenv("OPENAI_API_KEY", None)

    # manage message
    if isinstance(messages, BasePrompt):
        logging.info("messages is a BasePrompt")

        messages = messages.dictize()

    if not isinstance(messages, list):
        AttributeError(f"messages : {messages} => messages must be a lsit of dict")

    if not isinstance(messages[0], dict):
        raise AttributeError(
            f"message[0] :  {messages[0]} => messages[0] must be a dict"
        )

    # request
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=temperature,
    api_key=api_key)

    output = response.choices[0].message["content"]

    return output


# if __name__ == "__main__":
#     """ """

#     # logging
#     logging.basicConfig(level=logging.INFO)

#     # env
#     config = manage_env()

#     # data
#     data = "helloww mi name is Alex"

#     # insight
#     insight = "use a very slang or informal language"

#     # prompt
#     prompt = prompts.Insight(data, insight)

#     # completion
#     output = completion_from_messages(prompt, api_key=config["OPENAI_API_KEY"])

#     logging.info(f"output : {output}")
