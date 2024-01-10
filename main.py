"""
# main stremalit app
"""

import os
import logging

import sys

import streamlit as st

from jalait.core import Jalait
from jalait.front.corpus import Corpus
from jalait.front.inputs import Input

# import pandas as pd


#################################################################
#   HEADER
#################################################################

st.image(Corpus.img)
st.title(Corpus.title)
st.subheader(Corpus.subheader)
st.divider()
st.write(Corpus.welcome)
st.write(Corpus.joke)
st.divider()


#################################################################
#  INPUT
#################################################################

input_text = st.text_area(**Input.text)
lang_level = st.selectbox(**Input.lang_level)
lang_country = st.selectbox(**Input.lang_country)
fix_text = st.checkbox(**Input.fix_text)
grammar = st.checkbox(**Input.grammar)
idioms = st.checkbox(**Input.idioms)
audio = st.checkbox(**Input.audio)

if st.button("Submit"):
    jalait = Jalait(
        input_text,
        lang_level,
        lang_country,
        fix_text,
        grammar,
        audio,
    )

    out = jalait.run()

    st.text(out)
