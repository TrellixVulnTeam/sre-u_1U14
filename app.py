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
  #current_selection = list(q.keys())
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

questions_shuffled = shuffle(copy_questions)

@app.route('/')
def quiz():
 #questions_shuffled = shuffle(copy_questions)
 for i in copy_questions.keys():
  random.shuffle(copy_questions[i])
 return render_template('main.html', q = questions_shuffled, o = copy_questions)

@app.route('/solution', methods=['POST'])
def quiz_answers():
  # for i in copy_questions.keys():
  #   answered = request.form[i]
  #   if questions.original_questions[i][0] == answered:
  return render_template('quiz_solutions.html',q = questions_shuffled, o = copy_questions)


if __name__ == '__main__':
 app.run(debug=True)
