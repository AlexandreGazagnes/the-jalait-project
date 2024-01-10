import os

import logging

import sys

from jalait.predict import completion_from_messages
from jalait.env import manage_env
from jalait.prompts import *


class Jalait:
    """ """

    def __init__(
        self,
        input_text: str,
        lang_level: str = "Standard or daily",
        lang_country: str = "American",
        fix_text: bool = True,
        grammar: bool = True,
        audio: bool = False,
        idioms: bool = False,
    ) -> None:
        """ """
        self.input_text = input_text
        self.lang_level = lang_level
        self.lang_country = lang_country
        self.fix_text = fix_text
        self.grammar = grammar
        self.audio = audio
        self.idioms = idioms
        self.output = ""
        self.analysis = ""

        self.config = config = manage_env()
        self.api_key = config.get("OPENAI_API_KEY", "Error")

    def fix(self):
        # insight
        insight = ""
        if self.lang_level != "-":
            insight += f"Use a {self.lang_level} level of language. \n"
        if self.lang_country != "-":
            insight += f"Use a {self.lang_country} english vocabulary/style. \n"
        if self.idioms:
            insight += f"Do not hesitate to use specific {self.lang_country} idioms, in accordance to the {self.lang_level} level of language expected. \n"

        self.insight = insight

        # prompt
        prompt = Prompts.Insight(self.input_text, insight)

        # completion
        output = completion_from_messages(
            prompt.dictize(),
            api_key=self.api_key,
        )

        self.output = output

        return output

    def analyze(self):
        """ """

        prompt = Prompts.Analyze(self.input_text, self.output, self.insight)

        # completion
        analysis = completion_from_messages(
            prompt.dictize(),
            api_key=self.api_key,
        )

        self.analysis = analysis

        return analysis
