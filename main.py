# Title: Cookie & Session Difference by GitHub/kvnbbg (Kevin MARVILLE)

# app.py
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField
from random import randint, choice
import os
import logging
from threading import Timer

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a simple form with a submit button
class RandomDataForm(FlaskForm):
    submit = SubmitField('Generate Random Data')

# List of people with professions
people = [
    {'name': 'Alice', 'profession': 'Doctor'},
    {'name': 'Bob', 'profession': 'Engineer'},
    {'name': 'Charlie', 'profession': 'Artist'},
    {'name': 'Diana', 'profession': 'Teacher'},
    {'name': 'Ethan', 'profession': 'Chef'},
    {'name': 'Fiona', 'profession': 'Musician'},
]

# List of random comments
comments = [
    'Your outfit looks great today!',
    'Did you know that the Eiffel Tower can be 15 cm taller during the summer?',
    'I really appreciate your work!',
    'Have you ever tried learning a new language?',
    'Your smile is contagious!',
    'I recently read an interesting book about space travel.',
]

def generate_comment():
    person = choice(people)
    comment = choice(comments)
    return f'{person["name"]} ({person["profession"]}): {comment}'

def flash_comments():
    comment = generate_comment()
    flash(comment)
    logger.info(f'Generated comment: {comment}')
    # Schedule the next comment to be flashed
    Timer(randint(5, 15), flash_comments).start()

@app.route('/', methods=['GET', 'POST'])
def index():
    logger.info('Accessed the index page.')
    form = RandomDataForm()
    if form.validate_on_submit():
        # Generate random data and store in session
        user_id = str(randint(10000, 99999))
        session['user_id'] = user_id
        logger.info(f'Generated random user ID: {user_id} and stored in session.')
        # Start the comment flash loop
        flash_comments()
        return redirect(url_for('show_data'))
    return render_template('index.html', form=form)

@app.route('/show_data')
def show_data():
    user_id = session.get('user_id')
    if user_id is None:
        logger.warning('No user ID found in session, redirecting to index.')
        return redirect(url_for('index'))
    logger.info(f'Retrieved user ID from session: {user_id}')
    return render_template('show_data.html', user_id=user_id)

@app.route('/clear_session')
def clear_session():
    user_id = session.pop('user_id', None)
    if user_id:
        logger.info(f'Cleared user ID from session: {user_id}')
    else:
        logger.info('No user ID found in session to clear.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    logger.info('Starting the Flask application.')
    app.run(debug=True)