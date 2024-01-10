import pandas as pd
import json
import logging

from ._base import InsightBasePrompt


class InsightPromt(InsightBasePrompt):
    """Insight prompt for the user.

    Methods:
        - dictize() : return dict of messages
        - jsonize() : return json of messages
        - strize() : return str of messages
    """

    user_delimiter = "####"

    insight_delimiter = "===="

    system_message_template = """
You are an english teacher working for people who want to correct, to fix or to improve their english language skills. \

You will be provided a text written by a non english native student. \

You will have to correct the text given by the user, taking into account the user's specific criterias. \

The user query will be delimited with \
--USER_DELIMITER-- characters.

The user's specific criterias will be delimited with \
--INSIGHT_DELIMITER-- characters.

You will answer only in english language, and you will provide a text with good tense, grammar, and vocabulary. \

    """

    user_message_template = """
--USER_DELIMITER-- 
Correct this text for me : 
--DATA--
--USER_DELIMITER-- 


In your correction, try to take into account the language level and the language specification of various countries : \
--INSIGHT_DELIMITER--
--INSIGHT_DATA--
--INSIGHT_DELIMITER--
    """

    def __init__(
        self,
        data: str,
        insight: str | list | dict,
        user_delimiter: str = None,
        insight_delimiter: str = None,
        system_message_template: str = None,
        user_message_template: str = None,
    ) -> None:
        """ """

        super().__init__(
            data=data,
            insight=insight,
            user_delimiter=user_delimiter,
            insight_delimiter=insight_delimiter,
            system_message_template=system_message_template,
            user_message_template=user_message_template,
        )


# if __name__ == "__main__":
#     data = {"ca": 100}
#     insight = "le marché est tendax "
#     p = InsightPromt(data=data, insight=insight)
