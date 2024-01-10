"""
manage .env file and config file
"""


import os

# from load_dotenv import load_dotenv
from dotenv import dotenv_values


def manage_env(fn=".env/.env.prod"):
    """ """
    config = dotenv_values(fn)

    if not config:
        config = {
            # GENERIC
            "ENV": os.getenv("ENV", "LOCAL"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", None),
        }

    return dict(config)
