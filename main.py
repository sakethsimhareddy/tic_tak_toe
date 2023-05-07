from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("TIC TAK TOC")
game = True

global b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9
def button(mode):
    global b_1, b_2, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9
    b_1 = Button(root, text=" ", command=lambda: click(b_1, mode), padx=50, pady=50, font=30)
    b_2 = Button(root, text=" ", command=lambda: click(b_2, mode), padx=50, pady=50, font=30)
    b_3 = Button(root, text=" ", command=lambda: click(b_3, mode), padx=50, pady=50, font=30)
    b_4 = Button(root, text=" ", command=lambda: click(b_4, mode), padx=50, pady=50, font=30)
    b_5 = Button(root, text=" ", command=lambda: click(b_5, mode), padx=50, pady=50, font=30)
    b_6 = Button(root, text=" ", command=lambda: click(b_6, mode), padx=50, pady=50, font=30)
    b_7 = Button(root, text=" ", command=lambda: click(b_7, mode), padx=50, pady=50, font=30)
    b_8 = Button(root, text=" ", command=lambda: click(b_8, mode), padx=50, pady=50, font=30)
    b_9 = Button(root, text=" ", command=lambda: click(b_9, mode), padx=50, pady=50, font=30)
    b_exit = Button(root, text="exit", command=root.quit, padx=30, pady=20, font=20)
    b_reset = Button(root, text="reset ", command=lambda: reset(mode), padx=30, pady=20, font=20)

    b_7.grid(row=2, column=0)
    b_8.grid(row=2, column=1)
    b_9.grid(row=2, column=2)
    b_4.grid(row=1, column=0)
    b_5.grid(row=1, column=1)
    b_6.grid(row=1, column=2)
    b_1.grid(row=0, column=0)
    b_2.grid(row=0, column=1)
    b_3.grid(row=0, column=2)
    b_exit.grid(row=4, column=2)
    b_reset.grid(row=4, column=0)


def full_board(mode):

    if b_1["text"] != " " and b_2["text"] != " " and b_3["text"] != " " and b_4["text"] != " " and b_5[
        "text"] != " " and b_6["text"] != " " and b_7["text"] != " " and b_8["text"] != " " and b_9["text"] != " ":
        messagebox.showinfo("GAME OVER ", "IT'S DRAW")
        reset(mode)


def reset(mode):
    global lable
    global game
    global b_1, b_2, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9
    game = True

    lable.grid_forget()
    b_1.grid_forget()
    b_2.grid_forget()
    b_3.grid_forget()
    b_4.grid_forget()
    b_5.grid_forget()
    b_6.grid_forget()
    b_7.grid_forget()
    b_8.grid_forget()
    b_9.grid_forget()

    lable = Label(root, text="player 1", font=30)
    b_1 = Button(root, text=" ", command=lambda: click(b_1, mode), padx=50, pady=50, font=30)
    b_2 = Button(root, text=" ", command=lambda: click(b_2, mode), padx=50, pady=50, font=30)
    b_3 = Button(root, text=" ", command=lambda: click(b_3, mode), padx=50, pady=50, font=30)
    b_4 = Button(root, text=" ", command=lambda: click(b_4, mode), padx=50, pady=50, font=30)
    b_5 = Button(root, text=" ", command=lambda: click(b_5, mode), padx=50, pady=50, font=30)
    b_6 = Button(root, text=" ", command=lambda: click(b_6, mode), padx=50, pady=50, font=30)
    b_7 = Button(root, text=" ", command=lambda: click(b_7, mode), padx=50, pady=50, font=30)
    b_8 = Button(root, text=" ", command=lambda: click(b_8, mode), padx=50, pady=50, font=30)
    b_9 = Button(root, text=" ", command=lambda: click(b_9, mode), padx=50, pady=50, font=30)
    b_exit = Button(root, text="exit", command=root.quit, padx=30, pady=20, font=20)
    b_reset = Button(root, text="reset ", command=lambda: reset(mode), padx=30, pady=20, font=20)

    b_7.grid(row=0, column=0)
    b_8.grid(row=0, column=1)
    b_9.grid(row=0, column=2)
    b_4.grid(row=1, column=0)
    b_5.grid(row=1, column=1)
    b_6.grid(row=1, column=2)
    b_1.grid(row=2, column=0)
    b_2.grid(row=2, column=1)
    b_3.grid(row=2, column=2)
    lable.grid(row=3, column=0, columnspan=3)
    b_exit.grid(row=4, column=2)
    b_reset.grid(row=4, column=0)


def win(mode):
    if b_1["text"] == "X" and b_2["text"] == "X" and b_3["text"] == "X":
        b_1.config(bg="red")
        b_2.config(bg="red")
        b_3.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_4["text"] == "X" and b_5["text"] == "X" and b_6["text"] == "X":
        b_4.config(bg="red")
        b_5.config(bg="red")
        b_6.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_7["text"] == "X" and b_8["text"] == "X" and b_9["text"] == "X":
        b_7.config(bg="red")
        b_8.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_1["text"] == "X" and b_4["text"] == "X" and b_7["text"] == "X":
        b_1.config(bg="red")
        b_4.config(bg="red")
        b_7.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_2["text"] == "X" and b_5["text"] == "X" and b_8["text"] == "X":
        b_2.config(bg="red")
        b_5.config(bg="red")
        b_8.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_3["text"] == "X" and b_6["text"] == "X" and b_9["text"] == "X":
        b_3.config(bg="red")
        b_6.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_1["text"] == "X" and b_5["text"] == "X" and b_9["text"] == "X":
        b_1.config(bg="red")
        b_5.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_3["text"] == "X" and b_5["text"] == "X" and b_7["text"] == "X":
        b_3.config(bg="red")
        b_5.config(bg="red")
        b_7.config(bg="red")
        lable = Label(root, text="player 1 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        reset(mode)

    elif b_1["text"] == "O" and b_2["text"] == "O" and b_3["text"] == "O":
        b_1.config(bg="red")
        b_2.config(bg="red")
        b_3.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)


    elif b_4["text"] == "O" and b_5["text"] == "O" and b_6["text"] == "O":
        b_4.config(bg="red")
        b_5.config(bg="red")
        b_6.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_7["text"] == "O" and b_8["text"] == "O" and b_9["text"] == "O":
        b_7.config(bg="red")
        b_8.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_1["text"] == "O" and b_4["text"] == "O" and b_7["text"] == "O":
        b_1.config(bg="red")
        b_4.config(bg="red")
        b_7.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_2["text"] == "O" and b_5["text"] == "O" and b_8["text"] == "O":
        b_2.config(bg="red")
        b_5.config(bg="red")
        b_8.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_3["text"] == "O" and b_6["text"] == "O" and b_9["text"] == "O":
        b_3.config(bg="red")
        b_6.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_1["text"] == "O" and b_5["text"] == "O" and b_9["text"] == "O":
        b_1.config(bg="red")
        b_5.config(bg="red")
        b_9.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O Wins!!")
        reset(mode)

    elif b_3["text"] == "O" and b_5["text"] == "O" and b_7["text"] == "O":
        b_3.config(bg="red")
        b_5.config(bg="red")
        b_7.config(bg="red")
        lable = Label(root, text="player 2 winner")
        lable.grid(row=3, column=0, columnspan=3)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O  Wins!!")
        reset(mode)


def win_checker(p):
    if b_1["text"] == p and b_2["text"] == p and b_3["text"] == p:
        return True
    elif b_4["text"] == p and b_5["text"] == p and b_6["text"] == p:
        return True

    elif b_7["text"] == p and b_8["text"] == p and b_9["text"] == p:
        return True

    elif b_1["text"] == p and b_4["text"] == p and b_7["text"] == p:
        return True

    elif b_2["text"] == p and b_5["text"] == p and b_8["text"] == p:
        return True

    elif b_3["text"] == p and b_6["text"] == p and b_9["text"] == p:
        return True

    elif b_1["text"] == p and b_5["text"] == p and b_9["text"] == p:
        return True

    elif b_3["text"] == p and b_5["text"] == p and b_7["text"] == p:
        return True


def click(b, mode):
    global game
   

    if mode == 2:
        if b["text"] == " " and game is True:
            b["text"] = "X"
            game = False
            lable = Label(root, text="player 2", width=30)
            lable.grid(row=3, column=0, columnspan=3)
            win(mode)
            full_board(mode)

        elif b["text"] == " " and game is False:
            b["text"] = "O"
            game = True

            lable = Label(root, text="player 1", width=30)
            lable.grid(row=3, column=0, columnspan=3)
            win(mode)
            full_board(mode)
        else:
            messagebox.showinfo("error", "invalid choice")
    elif mode == 1:
        if b["text"] == " " and game is True:
            b["text"] = "X"
            game = False
            win(mode)
            full_board(mode)
        else:
            messagebox.showinfo("error", "invalid choice")
            full_board(mode)

        for i in (b_1, b_2, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9):
            if i["text"] == " " and game is False:
                i["text"] = "O"
                if win_checker("O"):
                    i["text"] = "O"
                    game = True
                else:
                    i["text"] = " "

        for i in (b_1, b_2, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9):
            if i["text"] == " " and game is False:
                i["text"] = "X"
                if win_checker("X"):
                    i["text"] = "O"
                    game = True
                else:
                    i["text"] = " "

        if game is False:
            l = (b_1, b_2, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9)
            while not game:
                j = random.randint(0, 8)
                if l[j]["text"] == " ":
                    l[j]["text"] = "O"
                    game = True

    full_board(mode)
    win(mode)


def play(mode):
    lable.grid_forget()
    b_c.grid_forget()
    b_p.grid_forget()
    button(mode)


lable = Label(root, text="WHAT WOULD YOU LIKE")
b_c = Button(root, text="PLAYER VS COMPUTER", command=lambda: play(1))
b_p = Button(root, text="PLAYER VS PLAYER", command=lambda: play(2))

lable.grid(row=0, column=0, columnspan=3, padx=60, pady=30)
b_c.grid(row=2, column=1, padx=60, pady=30)
b_p.grid(row=4, column=1, padx=60, pady=30)

root.mainloop()
