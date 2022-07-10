from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/')
def home():
    return render_template('instructions.html', title='Instructions')

@app.route('/<p1_choice>/<p2_choice>')
def play_url(p1_choice, p2_choice):
    player_1 = Player("Player 1", p1_choice)
    player_2 = Player("Player 2", p2_choice)

    winner = Game.play(player_1.name, player_1.choice, player_2.name, player_2.choice)
    
    
    return render_template('results.html', title="Results", player_1=player_1, player_2=player_2, winner=winner)


@app.route('/play')
def rps_form():
    return render_template('play.html', title='Play')


@app.route('/results', methods=['POST'])
def play_form():
    p1_choice = request.form["p1"]
    p2_choice = request.form["p2"]

    player_1 = Player("Player 1", p1_choice)
    player_2 = Player("Player 2", p2_choice)

    winner = Game.play(player_1.name, player_1.choice, player_2.name, player_2.choice)
    
    return render_template('results.html', title="Results", player_1=player_1, player_2=player_2, winner=winner)