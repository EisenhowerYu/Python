import tkinter as tk #tk-interface (GUI library)

# Constants
color_blu = "#4584b6"
color_ylw = "#ffde57"
color_gry = "#343434"
color_lgy = "#646464"

board = [[None for y in range(3)] for x in range(3)]
playerO = "O"
playerX = "X"
curr_player = playerX

turns = 0
game_over = False

# Functions

def set_tile(row, col):
  global curr_player

  if game_over: return

  if board[row][col]["text"] != "": return

  board[row][col]["text"] = curr_player

  # switch player after
  if curr_player == playerO:
    curr_player = playerX
  else:
    curr_player = playerO

  label["text"] = curr_player+"'s turn"
  
  check_winner(row, col)

def check_winner(row, col):
  global turns, game_over
  turns += 1

  # horizontally
  if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]:
    label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_ylw, background=color_lgy)

    for col2 in range(3):
      board[row][col2].config(foreground = color_ylw, background=color_lgy)

    game_over = True
    return

  # vertically, check 3 rows
  if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]:
    label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_ylw, background=color_lgy)

    for row2 in range(3):
      board[row2][col].config(foreground=color_ylw, background=color_lgy)

    game_over = True
    return

  # diagonally
  if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
    label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_ylw, background=color_lgy)

    for diag in range(3):
      board[diag][diag].config(foreground=color_ylw, background=color_lgy)

    game_over = True
    return

  if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
    label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_ylw, background=color_lgy)

    for diag in range(3):
      board[diag][2-diag].config(foreground=color_ylw, background=color_lgy)

    game_over = True
    return

  # no more turns
  if turns == 9:
    game_over = True
    label.config(text="Tie!", foreground=color_ylw)

def new_game():
  global turns, game_over

  turns = 0
  game_over = False

  label.config(text=curr_player + "'s turn", foreground="white", background=color_gry)

  for row in range(3):
    for col in range(3):
      board[row][col].config(text="", foreground="white", background=color_gry)
  
win = tk.Tk() # create game window
win.title("Test")
win.resizable(True, True)

frame = tk.Frame(win)

label = tk.Label(frame, text="X's turn", font=("Consolas", 20), background=color_gry, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
  for col in range(3):
    board[row][col] = tk.Button(frame, text="", font=("Consolas", 50, "bold"),
                                background=color_gry, foreground=color_blu,
                                width=4, height=1,
                                command=lambda row=row, col=col:set_tile(row, col))

    # arrange into the grid
    board[row][col].grid(row=row+1, column=col)

restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20),
                           background=color_gry,
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

## format: "(w)x(h)+(x)+(y)"
win.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

win.mainloop()