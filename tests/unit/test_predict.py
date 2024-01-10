import os
import logging

import pytest


from jalait.prompts import *
from jalait.env import manage_env
from jalait.predict import completion_from_messages

from pprint import pprint, pformat
from jalait.prompts.insight import InsightPromt


from jalait.front.inputs import Input

from itertools import product

user_input = Input.text.get("placeholder")

options = product(
    [
        user_input,
        "my neihgbor is an asshole because he is alaways making some fuking noise",
    ],
    [
        "slang or informal",
        "sustained or formal",
    ],
    [
        "american",
        "british",
    ],
)

# logging.critical(f"len options : {len(list(options))}")


class TestPredict:
    """ """

    @pytest.mark.parametrize("data,lang_level,lang_country", list(options))
    def test_predict(self, data, lang_level, lang_country):
        # env
        config = manage_env()

        # prompt
        insight = f"Use a {lang_level} level of language, and a {lang_country} english vocabulary/style."
        prompt = Prompts.Insight(data, insight)

        # completion
        output = completion_from_messages(
            prompt.dictize(),
            api_key=config["OPENAI_API_KEY"],
        )

        logging.info(f"output : {output}")


idea = "at the begining, i had started an simple learning AI bot, but with the time, and when the time was passing, i discover that i was coding a huge project"
