from flask import render_template
from app import app
from models.player import *
from models.game import *

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/<player-one-choice>/<player-two-choice>')
def play(p1_choice, p2_choice):
    player_1 = Player("Player_1", p1_choice)
    player_2 = Player("Player_2", p2_choice)
    
    game = Game.play(player_1.choice, player_2.choice)
    
    return render_template('results.html', title='Results', game=game)