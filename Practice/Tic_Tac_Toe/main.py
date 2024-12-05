import tkinter as tk #tk-interface (GUI library)

# Constants
color_blu = "#4584b6"
color_ylw = "#ffde57"
color_gry = "#343434"
color_lgy = "#646464"

board = [[None for y in range(3)] for x in range(3)]

# Functions

def set_tile(row, col):
  pass

def new_game():
  pass

win = tk.Tk() # create game window
win.title("Test")
win.resizable(True, True)

frame = tk.Frame(win)

label = tk.Label(frame, text="X's turn", font=("Times New Roman", 20), background=color_gry, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
  for col in range(3):
    board[row][col] = tk.Button(frame, text="", font=("Times New Roman", 50, "bold"),
                                background=color_gry, foreground=color_blu,
                                width=4, height=1,
                                command=lambda row=row, col=col:set_tile(row, col))

    # arrange into the grid
    board[row][col].grid(row=row+1, column=col)

restart_button = tk.Button(frame, text="Restart", font=("Times New Roman", 20), background=color_gry,
                           foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window
win.update()
win_width = win.winfo_width()
win_height = win.winfo_height()
scn_width = win.winfo_screenwidth()
scn_height = win.winfo_screenheight()

win_x = int((scn_width/2) - (win_width/2))
win_y = int((scn_height/2) - (win_height/2))

# format: "(w)x(h)+(x)+(y)"
win.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

win.mainloop()