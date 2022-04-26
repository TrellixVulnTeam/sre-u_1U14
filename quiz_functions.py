import questions
import streamlit as st

question_list = questions.questions_dic

def generate_questions():
    question_count = 1
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
            elif inner_key == 'option6':
                option5 = st.checkbox(inner_value)
        question_count += 1

def display_solution():
    q_and_a_count = 1
    st.title("Solution")
    for key,value in question_list.items():
        string_number = str(q_and_a_count)
        string_question = f"q"+string_number
        for inner_key, inner_value in value.items():
            if key == string_question and inner_key == "answer":
                #st.write(f'{string_number}. Correct answer: {inner_value}')
                st.text(f'{string_number}. Correct answer: {inner_value}')
            elif key == string_question and string_question == "q3" and inner_key =="Reason":
                st.text(f'Reason: {inner_value}')
        q_and_a_count += 1