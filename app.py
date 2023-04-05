from flask import Flask, render_template, request, redirect, url_for, flash, session
import config
import marvin_functions
import aifunctions

app = Flask(__name__, static_folder=config.UPLOAD_FOLDER)

app = Flask(__name__)

app.secret_key = 'your_secret_key'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('generate_question.html', **locals())

@app.route('/create_question', methods=['POST'])
def create_question():
    # Get the question data from the form
    subject = request.form.get('subject')
    level = request.form.get('level')
    topic = request.form.get('topic')

    # Call your function to create the question
    question = aifunctions.create_question(subject, level, topic)
    session["question"] = question

    # Redirect to the questions page
    return redirect(url_for('answer_question'))



@app.route('/answer_question', methods=['GET'])
def answer_question():
    question = session['question']
    return render_template('answer_question.html', **locals())



@app.route('/generate_question', methods=["GET", "POST"])
def somePage():
    return render_template('generate_question.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
