from flask import render_template
from app import app
from models.player import *
from models.game import *

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/<p1_choice>/<p2_choice>')
def play(p1_choice, p2_choice):
    player_1 = Player("Player 1", p1_choice)
    player_2 = Player("Player 2", p2_choice)

    winner = Game.play(player_1.name, player_1.choice, player_2.name, player_2.choice)
    
    return render_template('results.html', title="Results", player_1=player_1, player_2=player_2, winner=winner)