import os
import logging

import pytest

from jalait.prompts.basic import BasicPromt


class TestBasicBasePrompt:
    """"""

    def test_init(self):
        """ """

        data = "helloww mi name is Alex"
        prompt = BasicPromt(data)
        # assert x == "BasePrompt(ABC)"

        logging.warning(prompt.dictize())
