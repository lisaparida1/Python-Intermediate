from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONTNAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_text.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    web = website_text.get("1.0", 'end-1c')
    passwd = pass_text.get("1.0", 'end-1c')
    mail = email_text.get("1.0", 'end-1c')
    new_data = {
        web: {
            "email": mail,
            "password": passwd
        }
    }

    if len(web) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure all the fields are filled!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_text.delete("1.0", 'end')
            pass_text.delete("1.0", 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    web = website_text.get("1.0", 'end-1c')

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message="No Data file found!")
    else:
        if web in data:
            messagebox.showinfo(title=web, message=f"Details of entered website:\nEmail: {data[web]['email']}\nPassword: {data[web]['password']}")
        else:
            messagebox.showinfo(title="OOPS", message="No details for the website found!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
frame = Frame(master=window, width=500, height=500)
frame.pack()

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(140, 120, image=logo_image)
canvas.place(x=110, y=25)

web_label = Label(text="Website:", font=(FONTNAME, 11, "bold"))
web_label.place(x=40, y=270)

website_text = Text(height=1, width=22)
website_text.focus()
website_text.place(x=170, y=270)

email_label = Label(text="Email/Username:", font=(FONTNAME, 11, "bold"))
email_label.place(x=20, y=310)

email_text = Text(height=1, width=37)
email_text.insert(END, "xyz@gmail.com")
email_text.place(x=170, y=310)

pass_label = Label(text="Password:", font=(FONTNAME, 11, "bold"))
pass_label.place(x=40, y=350)

pass_text = Text(height=1, width=22)
pass_text.place(x=170, y=350)

search_btn = Button(text="Search", width=14, command=search_password)
search_btn.place(x=358, y=266)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.place(x=358, y=345)

add_btn = Button(text="Add", width=42, command=add)
add_btn.place(x=170, y=390)

window.mainloop()