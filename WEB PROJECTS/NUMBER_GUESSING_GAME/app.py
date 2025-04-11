from flask import Flask, request, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace 'your_secret_key' with your actual secret key


@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'GET':
        session['number_to_guess'] = random.randint(1, 100)
        session['attempts'] = 0
        session['animate'] = True
    message = ''
    if request.method == 'POST':
        if 'reset' in request.form:
            session.pop('number_to_guess', None)  # remove number_to_guess from session
            session.pop('attempts', None)  # remove attempts from session
            session['animate'] = True
            return redirect(url_for('guess_number'))
        guess = request.form.get('guess')
        if guess:
            guess = int(guess)
            session['attempts'] = session.get('attempts', 0) + 1
            number_to_guess = session.get('number_to_guess')
            if number_to_guess is not None:
                if guess < number_to_guess:
                    message = "Too low! Try again."
                elif guess > number_to_guess:
                    message = "Too high! Try again."
                else:
                    message = f"Congratulations! You found the number in {session['attempts']} attempts."
                    session.pop('number_to_guess', None)  # remove number_to_guess from session
                    session.pop('attempts', None)  # remove attempts from session
    return render_template('PROJECTS\NUMBER_GUESSING_GAME\templates\index.html', message=message, attempts=session.get('attempts'), animate=session.get('animate'))

if __name__ == '__main__':
    app.run(debug=True)
