from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

board_size = 4
board = [[0] * board_size for _ in range(board_size)]
score = 0

def add_new_tile():
    empty_cells = [(i, j) for i in range(board_size) for j in range(board_size) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def merge_line(line):
    non_zero = [num for num in line if num != 0]
    merged = []
    skip = False
    for i in range(len(non_zero)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(non_zero[i] * 2)
            global score
            score += non_zero[i] * 2
            skip = True
        else:
            merged.append(non_zero[i])
    return merged + [0] * (len(line) - len(merged))

def move(direction):
    global board
    moved = False
    for i in range(board_size):
        if direction in ['up', 'down']:
            line = [board[j][i] for j in range(board_size)]
        else:
            line = board[i]

        if direction in ['right', 'down']:
            line.reverse()

        new_line = merge_line(line)

        if direction in ['right', 'down']:
            new_line.reverse()

        if direction in ['up', 'down']:
            for j in range(board_size):
                if board[j][i] != new_line[j]:
                    moved = True
                board[j][i] = new_line[j]
        else:
            if board[i] != new_line:
                moved = True
            board[i] = new_line

    if moved:
        add_new_tile()
    return moved

def is_game_over():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return False
            if j + 1 < board_size and board[i][j] == board[i][j + 1]:
                return False
            if i + 1 < board_size and board[i][j] == board[i + 1][j]:
                return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init', methods=['GET'])
def initialize():
    global board, score
    board = [[0] * board_size for _ in range(board_size)]
    score = 0
    add_new_tile()
    add_new_tile()
    return jsonify({"board": board, "score": score})

@app.route('/move', methods=['POST'])
def move_board():
    direction = request.json.get('direction')
    if direction in ['up', 'down', 'left', 'right']:
        moved = move(direction)
        return jsonify({"board": board, "score": score, "game_over": is_game_over(), "moved": moved})
    return jsonify({"error": "Invalid direction"}), 400

if __name__ == '__main__':
    app.run(debug=True)