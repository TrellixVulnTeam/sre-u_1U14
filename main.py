from faulthandler import disable
import streamlit as st
import pandas as pd
import questions
import quiz_functions

st.title("Red Hat SRE-U Self Assessment")

quiz_functions.generate_questions()

submit_button = st.button("Submit")

if submit_button:
  quiz_functions.display_solution()