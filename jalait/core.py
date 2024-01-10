import os

import logging

import sys


class Jalait:
    """ """

    def __init__(
        self,
        input_text: str,
        lang_level: str,
        lang_country: str,
        fix_text: bool,
        grammar: bool,
        audio: bool,
    ) -> None:
        """ """
        self.input_text = input_text
        self.lang_level = lang_level
        self.lang_country = lang_country
        self.fix_text = fix_text
        self.grammar = grammar
        self.audio = audio

    def run(self):
        return """😠😠😠 Not implemented yet 😠😠😠"""
