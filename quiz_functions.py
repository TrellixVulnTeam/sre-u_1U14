import questions
import streamlit as st

question_list = questions.questions_dic

def generate_questions():
    question_count = 1
    for key,value in question_list.items():
        string_number = str(question_count)
        for inner_key, inner_value in value.items():
            if inner_key == 'question':
                question_output = st.write(f'**{string_number}. {inner_value}**')
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
        st.write('\n')

def display_solution():
    q_and_a_count = 1
    st.title("Solution")
    for key,value in question_list.items():
        string_number = str(q_and_a_count)
        string_question = f"q"+string_number
        for inner_key, inner_value in value.items():
            if inner_key == 'question':
                st.markdown(f"<p float:left; clear: both; style=color:Red;><strong>{string_number}. {inner_value}</strong></p>", unsafe_allow_html=True)
            if inner_key == "answer":
                st.markdown(f"<p float:left; clear: both;>{inner_value}</p>",unsafe_allow_html=True)
            elif string_question == "q3" and inner_key =="Reason":
                st.markdown(f'<p float:left; clear: both;> Reason: {inner_value}<p>',unsafe_allow_html=True)
        q_and_a_count += 1