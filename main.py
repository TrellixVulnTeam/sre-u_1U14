from faulthandler import disable
import streamlit as st
import pandas as pd
import questions
import quiz_functions


#def main():
st.title("Red Hat SRE-U Self Assessment")

quiz_functions.generate_questions()

submit_button = st.button("Submit")

if submit_button:
  quiz_functions.display_solution()


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

  # if __name__ == '__main__':
  #   main()
