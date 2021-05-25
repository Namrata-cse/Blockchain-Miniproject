import hashlib
import os
from tkinter import *
from tkinter import ttk
from client import *
from miner import *


class Login:
    def __init__(self, master):
        master.title("Login")
        master.geometry('400x150')
        btn1 = ttk.Button(master, text="Login As Student", width=20, command=lambda: self.btn(master, "Student")).grid(
            row=0, column=0, pady=10, padx=150)
        btn2 = ttk.Button(master, text="Login As Miner", width=20, command=lambda: self.btn(master, "Miner")).grid(
            row=1, column=0, padx=150)
        btn3 = ttk.Button(master, text="View Blocks", width=20, command=lambda: self.btn(master, "Blocks")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=10)
        btn4 = ttk.Button(master, text="Exit", width=20, command=lambda: self.btn(master, "Exit")).grid(row=3, column=0)

    def btn(self, master, log):
        master.withdraw()
        if (log == "Student"):
            form_window = Toplevel(master)
            new_form = Form(form_window, master)
        elif (log == "Miner"):
            # show transactions appended
            miner_window = Toplevel(master)
            new_mine = Miner(miner_window, master, last_block_hash)
            # to verify and mine
        elif (log == "Blocks"):
            block_window = Toplevel(master)
            block_window.title("Blocks")
            if (os.path.exists("blocks.txt")):
                f = open("blocks.txt", "r")
                blocks = f.read().split("\n")
                f.close()
                text = "\n".join(blocks)
                l = Label(block_window, text="Blocks")
                T = Text(block_window)
                T.insert(END, text)
                T.configure(state='disabled')
                b = Button(block_window, text="Exit", command=lambda: exit(block_window, master))
                l.pack()
                T.pack()
                b.pack()
            else:
                block_window.geometry('400x100')
                l = Label(block_window, text="No blocks in the chain")
                b = Button(block_window, text="Exit", command=lambda: exit(block_window, master))
                l.pack()
                b.pack()
        else:
            if (os.path.exists("results.txt")):
                os.remove("results.txt")
            if (os.path.exists("blocks.txt")):
                os.remove("blocks.txt")
            master.destroy()


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""


transactions = []
last_block_hash = ""
last_transaction_index = 0


def exit(block_window, master):
    block_window.destroy()
    master.deiconify()


def main():
    root = Tk()
    app = Login(root)
    root.mainloop()


if __name__ == '__main__':
    if (os.path.exists("results.txt")):
        os.remove("results.txt")
    if (os.path.exists("blocks.txt")):
        os.remove("blocks.txt")
    t0 = 'Genesis Block'
    # salt=os.urandom(8)
    digest = hash(t0)
    last_block_hash = digest
    main()
