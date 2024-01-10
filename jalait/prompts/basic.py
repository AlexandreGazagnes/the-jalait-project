import json

import pandas as pd

from ._base import BasicBasePrompt


class BasicPromt(BasicBasePrompt):
    """Basic prompt for the user.

    Methods:
        - dictize() : return dict of messages
        - jsonize() : return json of messages
        - strize() : return str of messages
    """

    user_delimiter = "####"

    system_message_template = """
You are an english teacher working for people who want to correct, to fix or to improve their english language skills. \

You will be provided a text written by a non english native student. \

You will have to correct the text given by the user, taking into account the user's specific criterias. \

The user query will be delimited with \
--USER_DELIMITER-- characters.

You will answer only in english language, and you will provide a text with good tense, grammar, and vocabulary. \
    """

    user_message_template = """
--USER_DELIMITER-- 
Correct this text for me : 
--DATA--
--USER_DELIMITER-- 

    """

    def __init__(
        self,
        data: str,
        user_delimiter: str = None,
        system_message_template: str = None,
        user_message_template: str = None,
    ) -> None:
        """ """

        super().__init__(
            data=data,
            user_delimiter=user_delimiter,
            system_message_template=system_message_template,
            user_message_template=user_message_template,
        )
