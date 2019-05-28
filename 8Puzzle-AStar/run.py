from flask import Flask, render_template, jsonify
import puzzle as p

puzzle = Flask(__name__)

@puzzle.route('/', methods=['GET'])
def main():
	p.init()
	initial = p.initial_state
	p.ast(initial)
	moves = p.backtrace()
	return render_template('main.html', initial=initial, moves=moves)

puzzle.run(debug=True)