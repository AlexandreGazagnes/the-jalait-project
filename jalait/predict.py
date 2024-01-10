"""
Prediction Module
"""

import os
import logging
import time

from openai import OpenAI

import pandas as pd

from jalait.prompts import InsightPromt, BasicPromt
from jalait.prompts import Prompts
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
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        # api_key=api_key
    )

    return response.choices[0].message.content
