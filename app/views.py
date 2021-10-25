from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message="Hello world!"
    return render_template('index.html',message=message) #The first message on the left of the = sign, represents the variable in the template. While the one to the right represents the variable in our view function.

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)