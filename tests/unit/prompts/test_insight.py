import os
import logging

import pytest


from pprint import pprint, pformat
from jalait.prompts.insight import InsightPromt


class TestInsightPromt:
    """"""

    def test_init(self):
        """ """

        data = "helloww mi name is Alex"
        insight = "use a very slang or informal language"
        prompt = InsightPromt(data, insight)
        # assert x == "BasePrompt(ABC)"

        _prompt = prompt.dictize()
        logging.warning(_prompt)

        sys_message = pformat(_prompt[0].get("content", "Error"))
        user_message = pformat(_prompt[1].get("content", "Error"))
        logging.warning(f"sys_message : {sys_message}")
        logging.warning(f"user_message : {user_message}")
