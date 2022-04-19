# import streamlit as st
# import pandas as pd
# import numpy as np

from flask import Flask, render_template, request
import random, copy
import questions
app = Flask(__name__)

copy_questions = copy.deepcopy(questions.original_questions)

def shuffle(q):
 """
 This function is for shuffling 
 the dictionary elements.
 """
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(list(q.keys()))
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

@app.route('/')
def quiz():
 questions_shuffled = shuffle(copy_questions)
 for i in copy_questions.keys():
  random.shuffle(copy_questions[i])
 return render_template('main.html', q = questions_shuffled, o = copy_questions)



if __name__ == '__main__':
 app.run(debug=True)























# st.title("SRE-U Self Assessment")

# q1choices = ('Foolish or boorish person.','A way to get and publish software packages ','A common unix command used to visualize code.','A source control tool.')
# list_q1choices = list(q1choices)
# q1_input = st.radio("1. What is git?",q1choices)
# # question, answer, solution

# for i in list_q1choices:
#     if i==list_q1choices[0]:
#         st.write("You got the right answer")
#         break
#     else:
#         st.write("wrong")
#         break
# # Need to have options for unseelct



# hide_st_style = """
#             <style>
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

