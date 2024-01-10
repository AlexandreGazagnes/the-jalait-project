import pandas as pd
import json

from abc import ABC

import logging


class BasePrompt(ABC):
    """Basic prompt for the user.

    Methods:
        - dictize() : return dict of messages
        - jsonize() : return json of messages
        - strize() : return str of messages
    """

    prompt_type = "base"
    user_delimiter = "<!> BASE USER DELIMITER <!>"
    insight_delimiter = "<!> BASE INSIGHT DELIMITER <!>"
    insight = "<!> BASE INSIGHT <!>"
    system_message_template = """"<!> BASE SYSTEM MESSAGE TEMPLATE <!>"""
    user_message_template = """"<!> BASE USER MESSAGE TEMPLATE <!>"""

    def __init__(
        self,
        data: str,
        insight: str = None,
        system_message_template: str = None,
        user_message_template: str = None,
        user_delimiter: str = None,
        insight_delimiter: str = None,
        prompt_type: str = None,
    ) -> None:
        """Build a system message from a template and a data

        Positional arguments:
            - data : pd.DataFrame | str | dict : data to use

        Optional arguments:
            - system_message_template : str : system message template
            - user_delimiter : str : user_delimiter for user
            - user_message_template : str : user message

        Returns:
            - system_message : dict[str:str] : system message
        """

        # logging.info("InsightBasePrompt ==>  __init__ CALLED")

        # args

        self.data = data
        self.insight = insight if insight else self.insight

        self.system_message_template = (
            system_message_template
            if system_message_template
            else self.system_message_template
        )

        self.user_message_template = (
            user_message_template
            if user_message_template
            else self.user_message_template
        )

        self.user_delimiter = user_delimiter if user_delimiter else self.user_delimiter
        self.insight_delimiter = (
            insight_delimiter if insight_delimiter else self.insight_delimiter
        )

        self.prompt_type = prompt_type if prompt_type else self.prompt_type

    def _build_system_message(self):
        raise AttributeError("ABC _build_system_message => Sould not be called")

    def _build_user_message(self):
        raise AttributeError("ABC _build_user_message_template => Sould not be called")

    def _build_messages(self):
        """build messages"""

        # logging.info("ABC => _build_messages => CALLED")

        system_content = self._build_system_message()
        user_content = self._build_user_message()

        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ]

        return messages

    def dictize(self) -> dict:
        """return dict of messages"""

        return self._build_messages()

    def jsonize(self) -> str:
        """ """

        raise NotImplementedError("not implemented yet")

    def strize(self) -> str:
        """ """

        messages_str = []

        for message in self._build_messages():
            tmp = f"{message['role']}:\n{message['content']}\n\n"
            messages_str.append(tmp)

        return "".join(messages_str)

    def __repr__(self) -> str:
        if self.prompt_type == "base":
            return "BasePrompt(ABC)"
        if self.prompt_type == "basic":
            return "BasicPrompt(BasicBasePrompt)"
        if self.prompt_type == "insight":
            return "InsightPrompt(InsightBasePrompt)"


class BasicBasePrompt(BasePrompt):
    """ """

    def __init__(
        self,
        data: str,
        system_message_template: str = None,
        user_message_template: str = None,
        user_delimiter: str = None,
    ) -> None:
        """ """

        # logging.info("BasicBasePrompt ==>  __init__ CALLED")

        super().__init__(
            data=data,
            system_message_template=system_message_template,
            user_message_template=user_message_template,
            user_delimiter=user_delimiter,
            prompt_type="basic",
        )

    def _build_system_message(self):
        """build system message from template and data"""

        # logging.info("BasicBasePrompt => _build_system_message => CALLED")

        system_message = self.system_message_template.replace(
            "--USER_DELIMITER--", self.user_delimiter
        )

        system_message = system_message.replace("\n\n", "\n").replace("\n\n", "\n")

        return system_message

    def _build_user_message(self):
        """_build_user_message"""

        # logging.info("BasicBasePrompt => _build_user_message => CALLED")

        user_message = self.user_message_template.replace(
            "--DATA--", str(self.data)
        ).replace("--USER_DELIMITER--", self.user_delimiter)

        return user_message


class InsightBasePrompt(BasePrompt):
    """ """

    def __init__(
        self,
        data: str,
        insight: str,
        system_message_template: str = None,
        user_message_template: str = None,
        user_delimiter: str = None,
        insight_delimiter: str = None,
    ) -> None:
        """ """

        # logging.info("InsightBasePrompt ==>  __init__ CALLED")

        super().__init__(
            data=data,
            insight=insight,
            system_message_template=system_message_template,
            user_message_template=user_message_template,
            user_delimiter=user_delimiter,
            insight_delimiter=insight_delimiter,
            prompt_type="insight",
        )

    def _build_system_message(self):
        """build system message from template and data"""

        # logging.info("InsightBasePrompt => _build_system_message => CALLED")

        # logging.info(f"self.system_message_template : {self.system_message_template}")

        system_message = self.system_message_template.replace(
            "--USER_DELIMITER--", self.user_delimiter
        ).replace("--INSIGHT_DELIMITER--", self.insight_delimiter)

        system_message = system_message.replace("\n\n", "\n").replace("\n\n", "\n")

        return system_message

    def _build_user_message(self):
        """build messages"""

        # logging.info("InsightBasePrompt => _build_user_message => CALLED")

        user_message = str(self.user_message_template)
        user_message = user_message.replace("--DATA--", str(self.data)).replace(
            "--USER_DELIMITER--", self.user_delimiter
        )

        user_message = user_message.replace(
            "--INSIGHT_DELIMITER--", self.insight_delimiter
        )
        user_message = user_message.replace("--INSIGHT_DATA--", self.insight)

        return user_message


class AnalyseBasePrompt(BasePrompt):
    """ """

    def __init__(
        self,
        input: str,
        output: str,
        insight: str,
        system_message_template: str = None,
        user_message_template: str = None,
        user_delimiter: str = None,
        insight_delimiter: str = None,
    ) -> None:
        """ """

        # logging.info("InsightBasePrompt ==>  __init__ CALLED")

        super().__init__(
            data=None,
            insight=insight,
            system_message_template=system_message_template,
            user_message_template=user_message_template,
            user_delimiter=user_delimiter,
            insight_delimiter=insight_delimiter,
            prompt_type="insight",
        )
        self.input = input
        self.output = output

    def _build_system_message(self):
        """build system message from template and data"""

        # logging.info("InsightBasePrompt => _build_system_message => CALLED")

        # logging.info(f"self.system_message_template : {self.system_message_template}")

        system_message = self.system_message_template.replace(
            "--USER_DELIMITER--", self.user_delimiter
        ).replace("--INSIGHT_DELIMITER--", self.insight_delimiter)

        system_message = system_message.replace("\n\n", "\n").replace("\n\n", "\n")

        return system_message

    def _build_user_message(self):
        """build messages"""

        # logging.info("InsightBasePrompt => _build_user_message => CALLED")

        user_message = str(self.user_message_template)
        user_message = (
            user_message.replace("--INPUT--", str(self.input))
            .replace("--OUTPUT--", str(self.output))
            .replace("--USER_DELIMITER--", self.user_delimiter)
        )

        user_message = user_message.replace(
            "--INSIGHT_DELIMITER--", self.insight_delimiter
        )
        user_message = user_message.replace("--INSIGHT_DATA--", self.insight)

        return user_message
