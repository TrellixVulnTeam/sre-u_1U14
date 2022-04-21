from faulthandler import disable
import streamlit as st
import pandas as pd

st.title("Red Hat SRE-U Self Assessment")

# genre = st.radio("Genre",('Comedy','Drama'),index=0)
# correct_genre = 'Comedy'

q1 = st.write("What is git?")
response1 = 'Foolish or boorish person.'
response2 = 'A way to get and publish software packages '
response3 = 'A common unix command used to visualize code.'
response4 = 'A source control tool.'

option1 = st.checkbox(response1)
option2 = st.checkbox(response2)
option3 = st.checkbox(response3)
option4 = st.checkbox(response4)


# if genre != "":
#   st.write(f'You selected {genre}')
# else:
#   st.write("No selection")

submit_button = st.button("Submit")

if submit_button:
  if option1 and not (option2 or option3 or option4):
    st.write(f'Correct Answer: {response1}')
  else:
    st.write(f'Correct Answer: {response1}')
  #if genre != "":
  # if genre:
  #   st.write(f'You selected {genre}')
  #   if genre==correct_genre:
  #     st.write(f'Correct Answer: {correct_genre}')
  #   else:
  #     st.write("Incorrect selection")


#if __name__ == '__main__':
