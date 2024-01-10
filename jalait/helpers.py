"""
Helpers functions 
"""

import secrets
import logging
import datetime
import json
import os


def now():
    """ """
    date = datetime.datetime.now()
    date = str(date)
    date = date[:19]
    date = date.replace(" ", "_").replace(":", "-")

    return date
