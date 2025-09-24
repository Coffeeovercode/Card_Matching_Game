import random
from guizero import App, Text, PushButton, Box, Window

class MemoryGame:


    def __init__(self, grid_size=4):
        # --- Game Configuration ---
        if grid_size % 2 != 0:
            grid_size += 1
        self.GRID_SIZE = grid_size
        self.CARD_SYMBOLS = ["🃏", "⭐", "🌙", "☀️", "❤️", "💎", "🚀", "🍀", "🍎", "🎁", "🎈", "🔑"]

        # --- Game State ---
        self.board_logic = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_active = True

        # --- UI Setup ---
        self.app = App(title="Memory Match", width=500, height=550, bg="#1a2b3c")

        # Header
        Text(self.app, text="Memory Match", size=24, font="Times New Roman", color="#ecf0f1")

        # Status Display
        self.status_box = Box(self.app, width="fill")
        self.status_text = Text(self.status_box, text="Make your first move!", color="#bdc3c7", size=14, font="Times New Roman")

        # Game Board Container -
        # This Box helps center the grid and maintain its square shape.(outer boundary, had to adjust this a bit)
        self.board_container = Box(self.app, width=400, height=400, border=False)
        self.board_box = Box(self.board_container, layout="grid", align="top")

        # 2D list to hold the PushButton widgets
        self.buttons = [[None] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

        self.setup_board()

        # Control Panel
        self.control_panel = Box(self.app, align="bottom", width="fill")
        self.reset_button = PushButton(self.control_panel, text="New Game", command=self.reset_game)
        # Fix: Improved button colors for visibility
        self.reset_button.bg = "#c0392b"
        self.reset_button.text_color = "white"
        self.reset_button.font = "Times New Roman"

        self.app.display()

    def setup_board(self):
        #creates the grid of cards and shuffles the symbols for a new game
        num_pairs = (self.GRID_SIZE * self.GRID_SIZE) // 2
        symbols_for_game = self.CARD_SYMBOLS[:num_pairs] * 2
        random.shuffle(symbols_for_game)
        
        self.board_logic = [[symbols_for_game.pop() for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]

        for y in range(self.GRID_SIZE):
            for x in range(self.GRID_SIZE):
                button = PushButton(
                    self.board_box,
                    text=" ",
                    grid=[x, y],
                    width=3,
                    height=2,
                    command=self.handle_card_click,
                    args=[x, y]
                )
                button.bg = "#3498db"
                button.text_size = 30
                self.buttons[x][y] = button

    def handle_card_click(self, x, y):
        #core game logic for when a player clicks a card.
        if not self.game_active or len(self.flipped_cards) >= 2:
            return

        clicked_button = self.buttons[x][y]
        
        if not clicked_button.enabled:
            return

        clicked_button.text = self.board_logic[x][y]
        clicked_button.bg = "#ecf0f1"
        clicked_button.disable()
        
        self.flipped_cards.append({"x": x, "y": y, "button": clicked_button})

        if len(self.flipped_cards) == 2:
            self.moves += 1
            self.update_status_text()
            self.check_for_match()

    def check_for_match(self):
        #checks if the two flipped cards are a match
        card1_data = self.flipped_cards[0]
        card2_data = self.flipped_cards[1]
        
        symbol1 = self.board_logic[card1_data["x"]][card1_data["y"]]
        symbol2 = self.board_logic[card2_data["x"]][card2_data["y"]]

        if symbol1 == symbol2:
            self.status_text.value = "You found a match!"
            self.matched_pairs += 1
            card1_data["button"].bg = "#2ecc71"
            card2_data["button"].bg = "#2ecc71"
            self.flipped_cards = []
            self.check_win_condition()
        else:
            self.status_text.value = "Not a match. Try again."
            self.game_active = False
            self.app.after(1000, self.flip_cards_back)

    def flip_cards_back(self):
        #resets the two non-matching cards back to their hidden state
        for card in self.flipped_cards:
            card["button"].text = " "
            card["button"].bg = "#3498db"
            card["button"].enable()
        self.flipped_cards = []
        self.game_active = True

    def update_status_text(self):
        #updates the text that shows the current move count
        self.status_text.value = f"Moves: {self.moves}"

    def check_win_condition(self):
        #checks if all pairs have been found
        total_pairs = (self.GRID_SIZE * self.GRID_SIZE) // 2
        if self.matched_pairs == total_pairs:
            self.game_active = False
            self.status_text.value = f"Congratulations! You won in {self.moves} moves!"
            self.show_win_window()

    def show_win_window(self):
        #displays a pop-up window to celebrate the win
        win_window = Window(self.app, title="You Won!", width=300, height=150, bg="#2c3e50")
        
        Box(win_window, height=20, width="fill")
        
        Text(win_window, text="You found all the matches!", size=14, font="Times New Roman", color="#ecf0f1")
        Text(win_window, text=f"Total Moves: {self.moves}", size=12, font="Times New Roman", color="#ecf0f1")
        
        self.app.when_closed = win_window.destroy

    def reset_game(self):
        #resets the entire board and game state for a new game
        for row in self.buttons:
            for button in row:
                button.destroy()

        self.matched_pairs = 0
        self.moves = 0
        self.flipped_cards = []
        self.game_active = True
        self.status_text.value = "Make your first move!"
        self.setup_board()


# --- Main Execution ---
if __name__ == "__main__":
    game = MemoryGame(grid_size=4)