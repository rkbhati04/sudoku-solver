import tkinter as tk
from tkinter import messagebox
import sudoku_solver

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        solve_btn = tk.Button(root, text="Solve", command=self.solve)
        solve_btn.grid(row=10, column=0, columnspan=9, sticky="we")

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center")
                e.grid(row=i, column=j, padx=2, pady=2)
                self.entries[i][j] = e

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val == "":
                    row.append(0)
                else:
                    try:
                        row.append(int(val))
                    except ValueError:
                        messagebox.showerror("Input Error", f"Invalid entry at ({i+1},{j+1})")
                        return None
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(board[i][j]) if board[i][j] != 0 else "")

    def solve(self):
        board = self.get_board()
        if board is None:
            return
        sudoku_solver.solveSudoku(board)
        self.set_board(board)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
