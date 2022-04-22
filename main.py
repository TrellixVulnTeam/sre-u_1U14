from faulthandler import disable
import streamlit as st
import pandas as pd
import questions

st.title("Red Hat SRE-U Self Assessment")

question_list = questions.questions_dic

question_count = 1
q_and_a_count = 1
for key,value in question_list.items():
  string_number = str(question_count)
  for inner_key, inner_value in value.items():
      if inner_key == 'question':
          question_output = st.write(f'{string_number}. {inner_value}')
      elif inner_key == 'option1':
          option1 = st.checkbox(inner_value)
      elif inner_key == 'option2':
          option2 = st.checkbox(inner_value)
      elif inner_key == 'option3':
          option3 = st.checkbox(inner_value)
      elif inner_key == 'option4':
          option4 = st.checkbox(inner_value)
      elif inner_key == 'option5':
          option5 = st.checkbox(inner_value)
    #break
    # This method did not work
  # string_number = str(q_and_a_count)
  # for inner_key, inner_value in value.items():
  #   if key == "q1" and inner_key == "answer":
  #     st.write(f'{string_number}. Correct answer: {inner_value}')

  question_count += 1

# submit_button = st.button("Submit")

# # if submit_button:
# #   q_and_a_count = 1
# #   for key,value in question_list.items():
# #     string_number = str(q_and_a_count)
# #     for inner_key, inner_value in value.items():
# #       if key == "q1" and inner_key == "answer":
# #         st.write(f'{string_number}. Correct answer: {inner_value}')
# #       elif key == "q2" and inner_key == "answer":
# #         st.write(f'{string_number}. Correct answer: {inner_value}')
# #     q_and_a_count += 1
