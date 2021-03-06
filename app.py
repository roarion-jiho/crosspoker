from flask import Flask, render_template
app = Flask(__name__)

import startgame, random

create_cards = list()

@app.route('/')
def start_game():
    global create_cards
    create_cards = startgame.card_info()
    game = startgame.hide_cards(create_cards)
    return render_template('basic.html', card = game[0], result_rows = game[1], result_columns = game[2], result_diagonals = game[3])

@app.route('/correctanswer')
def show_answer():
    global create_cards
    return render_template('answer.html', answer = create_cards[0])

if __name__ == '__main__':
    app.run(debug = True)