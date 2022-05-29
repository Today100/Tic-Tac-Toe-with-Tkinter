import tkinter as tk

root = tk.Tk()
root.title("Hello wold")
root.geometry("300x300")

current = "x"

def restart():
  global current
  for button in blocks:
    button["text"] = ""
    button["state"] = "normal"
    current = "x"
    win_label["text"] = ""
    c_label["text"] = "It is: " + current
    

def end_game(win):
  for button in blocks:
    button["state"] = "disabled"

  win_label["text"] = win + " wins!"
  restart.grid(row=5, columnspan=3)

def check_win():
  board = [[one["text"], two["text"], three["text"]],
          [four["text"], five["text"], six["text"]],
          [seven["text"], eight["text"], nine["text"]]]
  x_win = ["x", "x", "x"]
  o_win = ["o", "o", "o"]
  
  if board[0][:3] == x_win or board[1][:3] == x_win or board[2][:3] == x_win:
    end_game("x")
    
  if [n[0] for n in board ] == x_win or [n[1] for n in board] == x_win or [n[2] for n in board] == x_win:
    end_game("x")
  # print([[board[0][0]], [board[1][1]], [board[2][2]]])
  
  if [board[0][0], board[1][1], board[2][2]] == x_win or [board[0][2], board[1][1], board[2][0]] == x_win:
    end_game("x")

  if board[0][:3] == o_win or board[1][:3] == o_win or board[2][:3] == o_win:
    end_game("o")
    
  if [n[0] for n in board ] == o_win or [n[1] for n in board] == o_win or [n[2] for n in board] == o_win:
    end_game("o")
  # print([[board[0][0]], [boa/rd[1][1]], [board[2][2]]])
  
  if [board[0][0], board[1][1], board[2][2]] == o_win or [board[0][2], board[1][1], board[2][0]] == o_win:
    end_game("o")
  
  # print(board)

def change_text(x):
  global current
  # print(x["text"])
  
  x["text"] = current
  if current == "x":
    current = "o"
  else:
    current = "x"

  c_label["text"] = "It is: " + current
  check_win()

one = tk.Button(root, text=" ", command=lambda:change_text(one))
one.grid(row=0, column=0)
two = tk.Button(root, text=" ", command=lambda:change_text(two))
two.grid(row=0, column=1)
three = tk.Button(root, text=" ", command=lambda:change_text(three))
three.grid(row=0, column=2)
four = tk.Button(root, text=" ", command=lambda:change_text(four))
four.grid(row=1, column=0)
five = tk.Button(root, text=" ", command=lambda:change_text(five))
five.grid(row=1, column=1)
six = tk.Button(root, text=" ", command=lambda:change_text(six))
six.grid(row=1, column=2)
seven = tk.Button(root, text=" ", command=lambda:change_text(seven))
seven.grid(row=2, column=0)
eight = tk.Button(root, text=" ", command=lambda:change_text(eight))
eight.grid(row=2, column=1)
nine = tk.Button(root, text=" ", command=lambda:change_text(nine))
nine.grid(row=2, column=2)

restart = tk.Button(root, text="Restart?", command=restart)
restart.grid(row=5, columnspan=3)
restart.grid_forget()

c_label = tk.Label(root, text="It is: " + current)
c_label.grid(row=3)
win_label = tk.Label(root, text='')
win_label.grid(row=4, sticky=("nswe"))

blocks = [one, two, three, four, five, six, seven, eight, nine]

tk.mainloop()