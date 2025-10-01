# 🧠 Memory Match Game

A classic memory matching card game built with Python and the `guizero` library. The objective is to find all the matching pairs of cards in the fewest moves possible.



## Features

-   **Clean Graphical User Interface (GUI):** A simple and intuitive windowed application.
-   **Dynamic Grid Size:** Easily change the board size (e.g., 4x4, 6x6) by modifying a single variable.
-   **Move Counter:** Tracks the number of pairs you've attempted to match.
-   **Visual Feedback:** Cards change color to indicate a successful match or flip back over if they don't match.
-   **Win Condition:** A congratulatory pop-up window appears when you've successfully matched all the pairs.
-   **Replayability:** A "New Game" button allows you to reset the board and play again instantly.

---

## Requirements

-   Python 3
-   `guizero` library

---

## How to Run

1.  **Clone the repository or save the code:**
    Save your code into a file named `memory_game.py`.

2.  **Install the required library:**
    Open your terminal or command prompt and install `guizero` using pip:
    ```sh
    pip install guizero
    ```

3.  **Run the script:**
    Navigate to the directory where you saved the file and run the following command:
    ```sh
    python memory_game.py
    ```
    The game window should now appear on your screen.

---

## How to Play

1.  Click on any card to reveal its symbol.
2.  Click on a second card to see if it's a match.
3.  If the symbols on the two cards match, they will remain face-up.
4.  If they do not match, they will automatically flip back over after a brief delay.
5.  Continue flipping cards until you have matched all the pairs on the board.
6.  Your goal is to complete the game in as few moves as possible!

---

## Customization

You can easily customize the game by editing the script.

### Change Grid Size

To change the size of the grid, modify the `grid_size` number in the last line of the script. The grid size must be an even number.

```python
# --- Main Execution ---
if __name__ == "__main__":
    # Change the number 4 to 6 for a 6x6 grid, for example
    game = MemoryGame(grid_size=6)
```

### Add more symbols
```python
class MemoryGame:
    def __init__(self, grid_size=4):
        # ...
        self.CARD_SYMBOLS = ["🃏", "⭐", "🌙", "☀️", "❤️", "💎", "🚀", "🍀", "🍎", "🎁", "🎈", "🔑", "🎉", "💡", "🎸", "🍕"]
        # ...
```
