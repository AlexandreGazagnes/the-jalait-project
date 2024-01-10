import os
import logging

import pytest

from jalait.prompts._base import BasicBasePrompt, InsightBasePrompt


class TestBasePrompt:
    """"""

    def test_init(self):
        """ """

        data = "helloww mi name is Alex"
        prompt = BasicBasePrompt(data)
        # assert x == "BasePrompt(ABC)"

        logging.warning(prompt.dictize())


class TestInsightBasePrompt:
    """"""

    def test_init(self):
        """ """

        data = "helloww mi name is Alex"
        insight = "use a very slang or informal language"
        prompt = InsightBasePrompt(data, insight)
        # assert x == "BasePrompt(ABC)"

        logging.warning(prompt.dictize())
