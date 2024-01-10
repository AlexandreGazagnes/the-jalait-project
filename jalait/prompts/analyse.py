import pandas as pd
import json
import logging

from ._base import AnalyseBasePrompt


class AnalysePrompt(AnalyseBasePrompt):
    """Insight prompt for the user.

    Methods:
        - dictize() : return dict of messages
        - jsonize() : return json of messages
        - strize() : return str of messages
    """

    user_delimiter = "####"

    insight_delimiter = "===="

    system_message_template = """
You are an english teacher working for people who want to improve their english language skills. \

You will be provided two texts : 
- the first one is a wrong text, written by a student with a low knowledge of the english language
- the second one is the correction of the first text, written by a natuve english speaker \

You will have to explain the vocabulary, the grammar, the tenses difference. You will have to give detail on what are the the differences and why they are important. 

The wrong text will be delimited with \
--USER_DELIMITER-- characters.

The context of the correction will be delimited with \
--INSIGHT_DELIMITER-- characters.

You will answer only in english language, and you will as many explainations as possible on tense, idioms, grammar, and vocabulary. \

Try to structure your answer  as much as possible: Grammar, Tense, Vocabulary.
For each explanation, give exactly 3 examples of a good implementation of the concept.

    """

    user_message_template = """
--USER_DELIMITER-- 
Explain the differences between theses two texts : 

Wrong text is : 
--INPUT--

Corrected text is : 
--OUTPUT--

--USER_DELIMITER-- 


--INSIGHT_DELIMITER--
In your correction, try to take into account the language level and the language specification of various countries : \
--INSIGHT_DATA--
--INSIGHT_DELIMITER--
    """

    def __init__(
        self,
        input: str,
        output: str,
        insight: str | list | dict,
        user_delimiter: str = None,
        insight_delimiter: str = None,
        system_message_template: str = None,
        user_message_template: str = None,
    ) -> None:
        """ """

        super().__init__(
            input=input,
            output=output,
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
