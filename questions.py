import streamlit as st
questions_dic = {
    'q1': {
        'question':'What is git?',
        'option1': 'Foolish or boorish person.',
        'option2': 'A way to get and publish software packages ',
        'option3': 'A common unix command used to visualize code.',
        'option4': 'A source control tool.',
        'answer': 'Foolish or boorish person.'
    },
    'q2': {
        'question':'What is a public repository?',
        'option1': 'One in which developers by default have full edit privileges.',
        'option2': 'A repository globally accessible within the organization.',
        'option3': 'A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.',
        'option4': 'An open source repository.',
        'answer': 'A repository that has been made publicly viewable, meaning it can be forked and viewed by anyone, but maintainers control the commits.'
    },
}

# for key,value in questions_dic.items():
#     for inner_key, inner_value in value.items():
#         if inner_key == 'question':
#             #question_output = st.write(inner_value)
#             pass
#         elif inner_key == 'option1':
#             st.checkbox(inner_value)
#         elif inner_key == 'option2':
#             st.checkbox(inner_value)
#         elif inner_key == 'option3':
#             st.checkbox(inner_value)
#         elif inner_key == 'option4':
#             st.checkbox(inner_value)
#         elif inner_key == 'option5':
#             st.checkbox(inner_value)
#     break
