"""
# main stremalit app
"""

import os
import logging

import sys

import streamlit as st

from jalait.core import Jalait


# import pandas as pd


st.image("./assets/image.png")

st.title("The-Jalait-Project")
st.subheader(
    """        
👉 Give me your text and I'll be happy to correct and improve it. 
"""
)

st.divider()


st.write(
    """
🤖 Hello, I'm Jalait, your English language assistant.

💡 If you wish, I can provide explanations and context to help you improve your writing.

I can also read you the text to help you with your writing or pronunciation, depending on your level of speech or even your country.
"""
)

st.write("😎 Jalait stands for Just Another Learning AI Tool")


st.divider()

input_text = st.text_area(
    "📄 Please enter your text here",
    placeholder="""I have wrotten a veri bad text in english due to the fact that i am not very good at english.""",
)

lang_level = st.selectbox(
    "📢 Language Level",
    [
        "1 - slang/casual",
        "2 - normal/usual",
        "3 - sustained/formal",
    ],
)


lang_country = st.selectbox("🌏 Country", ["-", "US", "UK", "NZ", "AUST"])

fix_text = st.checkbox("✅ Fix the text", value=True)
grammar = st.checkbox("👩‍🏫 Give grammar, vocal and pronunciation feedback", value=True)
audio = st.checkbox("🔉 Provide Audio Output", value=False)

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
    # st.write("language level: ", lang_level)
    # st.write("language country: ", lang_country)
    # st.write("fix_text: ", fix_text)
    # st.write("grammar: ", grammar)
    # st.write("audio: ", audio)
