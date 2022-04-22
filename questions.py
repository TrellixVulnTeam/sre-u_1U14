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
    'q3': {
        'question':'How can main branches be used?',
        'option1': 'As the location for every commit to the repository of code by developers.',
        'option2': 'As the branch where only stable tested code is committed and released from.',
        'option3': 'To be used a honeypot to misdirect bad actors and bots.',
        'option4': 'The default first branch for any repository, but it can be removed or renamed per developer preferences. ',
        'answer' : 'As the location for every commit to the repository of code by developers.\nTo be used a honeypot to misdirect bad actors and bots.\n\nThe default first branch for any repository, but it can be removed or renamed per developer preferences. '
    },
}
