
   
from flask import Flask, render_template, redirect, url_for
from questions import PopQuiz


#SECRET_KEY = 'this is a secret key'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():
    form = PopQuiz()
    if form.validate_on_submit():
        return redirect(url_for('quiz_solution'))
        #return redirect(url_for('quiz_solutions'))
    #return render_template('quiz.html', form=form)
    return render_template('main.html',form=form)


@app.route('/quiz_solutions')
def quiz_solution():
    #return render_template('passed.html')
    return render_template('quiz_solutions.html')


if __name__ == '__main__':
    app.run(debug=True)