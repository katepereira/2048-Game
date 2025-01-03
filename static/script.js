let board = [];
let score = 0;

document.addEventListener("DOMContentLoaded", () => {
    const boardElement = document.getElementById("board");
    initializeBoard(boardElement);

    // Fetch the initial game state from the server
    fetch('/init')
        .then(response => response.json())
        .then(data => {
            board = data.board;
            score = data.score;
            updateBoard();
        })
        .catch(error => console.error("Error initializing game:", error));

    // Listen for arrow key presses to move tiles
    document.addEventListener("keydown", handleKeyPress);
});

// Function to initialize the board in the DOM
function initializeBoard(boardElement) {
    boardElement.style.gridTemplateColumns = `repeat(4, 1fr)`;
    boardElement.style.gridTemplateRows = `repeat(4, 1fr)`;

    // Create a grid of tiles
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const tile = document.createElement("div");
            tile.className = "tile";
            tile.id = `tile-${i}-${j}`;
            boardElement.appendChild(tile);
        }
    }
}

// Function to update the board UI
function updateBoard() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const tile = document.getElementById(`tile-${i}-${j}`);
            const value = board[i][j];
            tile.textContent = value === 0 ? "" : value;
            tile.className = `tile tile-${value}`;
        }
    }
    document.getElementById("score").textContent = `Score: ${score}`;
}

// Function to handle key presses for moves
function handleKeyPress(event) {
    const key = event.key;
    let direction;

    // Map arrow keys to move directions
    if (key === "ArrowUp") direction = "up";
    else if (key === "ArrowDown") direction = "down";
    else if (key === "ArrowLeft") direction = "left";
    else if (key === "ArrowRight") direction = "right";

    if (direction) {
        // Send move request to the server
        fetch('/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ direction: direction })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                board = data.board;
                score = data.score;
                updateBoard();

                // Check for game over
                if (data.game_over) alert("Game Over!");
            }
        })
        .catch(error => console.error("Error making move:", error));
    }
}
