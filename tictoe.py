from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("400x500")
win.config(bg="grey")
win.resizable(False, False)
win.title("Tic Tac Toe")

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

task = "X"
winner = None

frame_1 = Frame(win, height=50, width=400, bg="sky blue")
frame_1.place(x=0, y=0)

frame_2=Frame(win,height=450,width=400,bg="light blue")
frame_2.place(x=0,y=50)

label_1 = Label(frame_1, text="TIC TAC TOE", font=("Times New Roman", 40, "bold"), bg="sky blue")
label_1.place(x=50, y=0)


def check_winner():
    global winner
    winning_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                          (1, 4, 7), (2, 5, 8), (3, 6, 9),
                          (1, 5, 9), (3, 5, 7))

    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            winner = board[condition[0]]
            return True

    if all(value != " " for value in board.values()):
        winner = "Draw"
        return True

    return False


def click_event(i):
    global task
    if buttons[i].cget("text") == "" and not winner:
        buttons[i].config(text=task)
        board[i] = task
        if check_winner():
            show_result(winner)
        else:
            task = "O" if task == "X" else "X"


def show_result(winner):
    # Disable only game buttons
    for button in win.winfo_children():
        if isinstance(button, Button) and button != reset_button:
            button.config(state=DISABLED)
    messagebox.showinfo("Result", f"{winner} Wins!" if winner != "Draw" else "It's a Draw!")


def reset_game():
    global board, task, winner
    board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}
    task = "X"
    winner = None

    for button in win.winfo_children():
        if isinstance(button, Button):
            button.config(state=NORMAL, text="")


buttons = {}
for i in range(1, 10):
    row = (i - 1) // 3
    col = (i - 1) % 3
    button = Button(frame_2, text="", font=("Times New Roman", 25, "bold"), relief="raised", bd=1, width=5, height=3, command=lambda i=i: click_event(i))
    button.place(x=40+col * 100, y=80 + row * 100)  
    buttons[i] = button



reset_button = Button(win, text="Reset", font=("Times New Roman", 15, "bold"), command=reset_game)
reset_button.place(x=150, y=450)

win.mainloop()