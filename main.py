import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x400")


root = tk.Frame(window)
root.pack(anchor="center")

# orig_color = one["background"]

current = "x"
back_color = "yellow"


x_score = 0
o_score = 0
# class score_track():




def change_score(which):
  global x_score, o_score
  # global x_win, o_win, x_winButton, o_winButton
  if which == "x":
    x_score += 1
  elif which == "o":
    o_score += 1
  
  print(x_score)
  x_winButton["text"] = "X: " + str(x_score)
  o_winButton["text"] = "O: " + str(o_score)

def decrease(which):
  global x_score, o_score
  # global x_win, o_win, x_winButton, o_winButton
  print(which)
  if which == "x" and x_score != 0:
    x_score -= 1
  elif which == "o" and o_score != 0:
    o_score -= 1
  
  print(x_score)
  x_winButton["text"] = "X: " + str(x_score)
  o_winButton["text"] = "O: " + str(o_score)

    
def score_tracker():
  # global x_winButton, o_winButton, x_win, o_win
  print("here")
  # score_win = tk.Toplevel(window)
  score.deiconify()
  
  


# region  Here are the functions
def set_color():
  # print("runned")
  # print(colored.get())
  if colored.get():
    for button in blocks:
      if button["text"] == "x":
        button["background"] = "yellow"
      elif button["text"] == "o":
        button["background"] = "white"
  elif not colored.get():
    # print(orig_color)
    for button in blocks:
      button["background"] = orig_color


def restart():
  global current, back_color
  win_label["text"] = ""
  restart_b.grid_forget()
  back_color = "yellow"
  for button in blocks:
    button["text"] = ""
    button["state"] = "normal"
    current = "x"
    c_label["text"] = "It is: " + current
    button["background"] = orig_color
    

def end_game(win):
  # print(win, "winned")
  for button in blocks:
    button["state"] = "disabled"
  if tracker.get():
    change_score(win)
  win_label["text"] = win + " wins!"
  restart_b.grid(row=5, columnspan=3, padx=15, pady=15)

def check_win():
  board = []
  for button in blocks:
    board.append(button["text"])
  x_win = ["x", "x", "x"]
  o_win = ["o", "o", "o"]
  
  if board[:3] == x_win or board[3:6] == x_win or board[6:] == x_win: #Horizontal
    # print("checked first")
    end_game("x")
    
  elif [board[0],board[3], board[6]] == x_win or [board[1],board[4],board[7]] == x_win or [board[2], board[5], board[8]] == x_win: #Vertical
    end_game("x")
  # print([[board[0][0]], [board[1][1]], [board[2][2]]])
  
  elif [board[0], board[4], board[8]] == x_win or [board[2], board[4], board[6]] == x_win:  #Diagnal
    end_game("x")

  elif board[:3] == o_win or board[3:6] == o_win or board[6:] == o_win:
    end_game("o")
    
  elif [board[0],board[3], board[6]] == o_win or [board[1],board[4],board[7]] == o_win or [board[2], board[5], board[8]] == o_win:
    end_game("o")
  # print([[board[0][0]], [boa/rd[1][1]], [board[2][2]]])
  
  elif [board[0], board[4], board[8]] == o_win or [board[2], board[4], board[6]] == o_win:
    end_game("o")
  

  elif board.count("x") == 5 and board.count("o") == 4:
    # print("check last")
    end_game("None")


def change_text(x):
  global current, back_color
  # print(x["text"])
  if not colored.get():
    back_color = orig_color

  x["text"] = current
  x["state"] = tk.DISABLED
  x["background"] = back_color
  x['foreground'] = "black"

  if current == "x":
    current = "o"
    back_color = "white"
  else:
    current = "x"
    back_color = "yellow"

  c_label["text"] = "It is: " + current
  check_win()
# endregion



rowNum = 0
columnNum = 0
blocks = []

for x in range(9):
  buttons = tk.Button(root, text=" ", command=lambda x=x:change_text(blocks[x]), width=10, height=5, disabledforeground="black", font=(16), name=str(x))
  buttons.grid(row=rowNum, column=columnNum)
  columnNum += 1
  if columnNum == 3:
    rowNum += 1
    columnNum = 0
  blocks.append(buttons)

restart_b = tk.Button(root, text="Restart?", command=restart)
restart_b.grid(row=5, columnspan=3, padx=25, pady=25)
restart_b.grid_forget()

c_label = tk.Label(root, text="It is: " + current, font=(16))
c_label.grid(row=3, columnspan=3)
win_label = tk.Label(root, text='', font=("bold", 20))
win_label.grid(row=4, sticky=("nswe"), columnspan=3)


score = tk.Toplevel(window)
x_winButton = tk.Button(score, text="X: " + str(x_score), width=10, height=3, font=("bold", 16), command=lambda: change_score("x"))
o_winButton = tk.Button(score, text="O: " + str(o_score), width=10, height=3, font=("bold", 16), command=lambda: change_score("o"))
x_winButton.pack(side=tk.LEFT, fill="both", expand=True)
o_winButton.pack(side=tk.LEFT, fill="both", expand=True)
x_winButton.bind("<Button-3>", lambda e=None: decrease("x"))
o_winButton.bind("<Button-3>", lambda e=None: decrease("o"))
score.withdraw()

score.protocol("WM_DELETE_WINDOW", lambda: score.withdraw())

window.focus()


orig_color = blocks[0]["background"]



mainmenu = tk.Menu(window)

colored = tk.BooleanVar(value=1)
tracker = tk.BooleanVar(value=0)

setting = tk.Menu(mainmenu, tearoff=0)
setting.add_checkbutton(label="show color", command=set_color, variable=colored)
setting.add_command(label="Score Tracker", command=score_tracker)
setting.add_checkbutton(label="Automatic Track Score", variable=tracker, command=lambda: score.deiconify())
mainmenu.add_cascade(label='Setting', menu=setting)

window.config(menu=mainmenu)


tk.mainloop()