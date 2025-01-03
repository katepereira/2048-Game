# 2048 Game

A web-based implementation of the popular 2048 game built with Python (Flask) and JavaScript. The game allows you to slide tiles on a 4x4 grid to combine numbers and achieve the coveted 2048 tile.

## Features
- Interactive gameplay with arrow key controls.
- Score tracking.
- Responsive and visually appealing UI.
- Built using Flask as the backend and vanilla JavaScript for the frontend.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Code Overview](#code-overview)
5. [Screenshots](#screenshots)
6. [Future Enhancements](#future-enhancements)

## Getting Started
To play the game, clone the repository, install the dependencies, and run the application. The game runs locally in your browser.

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/2048-game.git
    cd 2048-game
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install flask
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the game in your browser: Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## How to Play
- Use the arrow keys on your keyboard to move tiles.
- Tiles with the same number merge into one when they touch.
- Try to reach the 2048 tile to win the game!
- If no more moves are possible, the game ends.

## Code Overview
- **Backend**: Flask is used to serve the game and handle requests.
- **Frontend**: The game’s frontend is built using vanilla JavaScript, HTML, and CSS.
- **Game Logic**: The logic for tile movement and merging is handled in the JavaScript file.

