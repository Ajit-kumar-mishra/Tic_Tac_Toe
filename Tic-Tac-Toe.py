import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Helvetica", 24), width=6, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            elif "" not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def show_winner(self):
        winner = self.current_player
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_board()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
