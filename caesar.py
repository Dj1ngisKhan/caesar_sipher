import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
import time
import random


# Window Set up:

window = tk.Tk()
window.geometry("700x300")
window.title("Caesar Cipher")
window.configure(bg='#efb036')

canvas = tk.Canvas(window, bg="#efb036", width=700, height=300)


# Variables:

options = ["Encrypt", "Decrypt", "Brute force"]
clicked = tk.StringVar()
clicked.set("Options")
chng = tk.StringVar()
chng.set("Button")
variable = ""
random_seed = random.choice(range(0,1000000))
latin = (list("¨^a@bc*defg8)hi\jk1l29m3no?.pq!r4'stu¤$567vw%xy([,zå]äö0"))
brute_list = []



def get_obj(event=None):
    global variable
    variable = clicked.get()
    chng.set(variable)


canvas.create_line(20, 15, 190, 15, width=2)
canvas.create_line(20, 45, 190, 45, width=1)
canvas.create_line(30, 60, 30, 270, width=2, dash=(1))
canvas.pack()

rubrik = tk.Label(window, text="Caesar Cipher", fg="black", bg="#efb036", font=("Courier New", 16))
rubrik.place(x=20, y=15)


msg_label = tk.Label(window, text="Message:", fg="black", bg="#F2B90C", font=("Courier New", 14))
key_label = tk.Label(window, text="Key:", fg="black", bg="#F2B90C", font=("Courier New", 14))
msg_bar = tk.Text(window, height=2, width=40, wrap="word", fg="#90EE90", relief="solid", bd=2, bg="#23486a",
font=("Sans serif", 12))
msg_bar.place(x=180, y=135)
key_bar = tk.Text(window, height=2, width=10, wrap="word", fg="#90EE90", bg="#3b6790", relief="solid",
bd=2, font=("Sans serif", 12))
key_bar.place(x=300, y=190)

msg_string = tk.Label(window, text="Msg:", fg="black", bg="#efb036", font=("Courier New", 14))
msg_string.place(x=85, y=140)
key_string = tk.Label(window, text="Key:", fg="black", bg="#efb036", font=("Courier New", 14))
key_string.place(x=210, y=195)

answer_var = tk.StringVar()
answer_var.set("")

answer = tk.Label(window, height=1, width=30, fg="black", textvariable=answer_var, bg="#efb036", font=("Courier New", 14))
answer.place(x=170, y=90)

dropdown = tk.OptionMenu(window, clicked, *options, command=get_obj)
dropdown.config(bg="#4c7b8b", fg="black", activebackground="#4c7b8b", activeforeground="black", borderwidth=2,
                width=6, height=1)
dropdown.place(x=560, y=50)


def main_func():

    def encryption_func():
        print("encrypt")
        if len(msg_bar.get("1.0", tk.END)) < 2:
            print("You need to input a message to encrypt!")
            exit()
        if len(key_bar.get("1.0", tk.END)) < 2:
            print("You need to input an encryption key!")
            exit()
        try:
            int(key_bar.get("1.0", tk.END))
        except Exception:
            print("Key needs to be of type integer!")
            exit()
        msg = (msg_bar.get("1.0", tk.END)).lower()
        key = int(key_bar.get("1.0", tk.END))
        new_msg = ""
        count = 1

        for stav in msg:
            if count == len(msg):
                break
            while True:
                if stav == " ":
                    new_msg += " "
                    count += 1
                    break
                else:
                    try:
                        new_msg += latin[latin.index(stav) + key]
                        count += 1
                        break
                    except Exception:
                        key = key - len(latin)
        answer_var.set(new_msg)

    def decryption_func():
        print("decrypting")
        if len(msg_bar.get("1.0", tk.END)) < 2:
            print("You need to input a message to decrypt!")
            exit()
        if len(key_bar.get("1.0", tk.END)) < 2:
            print("You need to input a decryption key!")
            exit()
        try:
            int(key_bar.get("1.0", tk.END))
        except Exception:
            print("Key needs to be of type integer!")
            exit()

        krypt_msg = msg_bar.get("1.0", tk.END).lower()
        de_key = int(key_bar.get("1.0", tk.END))
        count2 = 1
        dekrypt_msg = ""
        decrypt_key = 0

        for bit in krypt_msg:
            if count2 == len(krypt_msg):
                break
            while True:
                if bit == " ":
                    dekrypt_msg += " "
                    count2 += 1
                    break
                try:
                    decrypt_key = latin.index(bit) - de_key
                    dekrypt_msg += latin[decrypt_key]
                    count2 += 1
                    break
                except Exception:
                    de_key = de_key - len(latin)

        answer_var.set(dekrypt_msg)

    def brute_func():
        print("brute force")
        if len(msg_bar.get("1.0", tk.END)) < 2:
            print("You need to input a message to encrypt!")
            exit()

        brute_message = msg_bar.get("1.0", tk.END).lower()
        possible_keys = len(latin)-1
        for i in range(0, possible_keys):
            meddelande = ""
            for j in brute_message:
                if j == " ":
                    meddelande += " "
                else:
                    try:
                        meddelande += latin[latin.index(j) - i]
                    except Exception:
                        pass

            brute_list.append(meddelande)


            '''
            [[., .],
            [., .],
            [., .],
            [., .]]
        '''

        brute_diagram = np.full(shape=(possible_keys, 2), fill_value=".", dtype='<U100')
        #print(brute_diagram[:,0])
        brute_diagram[:,0] = range(0,possible_keys)
        brute_diagram[:,1] = brute_list

        df = pd.DataFrame(brute_diagram, columns=["Key", "Message"])
        #del pd_dia["Key"]
        df.set_index("Key", inplace=True)


        root = tk.Tk()
        root.title("Bruteforce Messages")

        text_widget = tk.Text(root, height=20, width=70)
        text_widget.pack(padx=10, pady=10)

        for key, message in df.iterrows():
            text_widget.insert(tk.END, f"Key: {key}\nMessage: {message['Message']}\n\n")

        text_widget.config(state=tk.DISABLED)

        root.mainloop()



    if variable == "Encrypt":
        encryption_func()
    elif variable == "Decrypt":
        decryption_func()
    elif variable == "Brute force":
        brute_func()

send_btn = tk.Button(window, textvariable=chng, width=10, height=1, command=main_func, bg="#4c7b8b",
activebackground="yellow")
send_btn.place(x=565, y=220)

window.mainloop()



