import os
import logging

import pytest


from pprint import pprint, pformat
from jalait.prompts.analyse import AnalysePrompt


class TestAnalysePrompt:
    """"""

    def test_init(self):
        """ """

        input = "at the begining, i had started an simple learning AI bot, but with the time, and when the time was passing, i discover that i was coding a huge project"
        output = "At the beginning, I started a simple learning AI bot. However, as time passed, I realized that I was actually coding a massive project."
        insight = "use a very slang or informal language in british language"
        prompt = AnalysePrompt(input, output, insight)
        # assert x == "BasePrompt(ABC)"

        _prompt = prompt.dictize()
        logging.warning(_prompt)

        sys_message = pformat(_prompt[0].get("content", "Error"))
        user_message = pformat(_prompt[1].get("content", "Error"))
        logging.warning(f"sys_message : {sys_message}")
        logging.warning(f"user_message : {user_message}")
