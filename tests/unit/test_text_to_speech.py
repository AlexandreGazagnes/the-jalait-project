import pytest

from transformers import pipeline
from IPython.display import Audio


def test_text_to_speech():
    """ """

    pipe = pipeline("text-to-speech", model="suno/bark-small")
    text = "[clears throat] This is a test ... and I just took a long pause."
    output = pipe(text)
    Audio(output["audio"], rate=output["sampling_rate"])
