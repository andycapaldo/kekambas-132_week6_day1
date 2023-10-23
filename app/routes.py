from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'andy'
    return render_template('index.html', name=name)


@app.route('/top5')
def top5():
    players = ['Nikola Jokic', 'Lebron James', 'Giannis Antetokounmpo', 'Steph Curry', 'Luka Doncic']
    return render_template('top5.html', players=players)