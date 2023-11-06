from tkinter import *
from conversion import Convert

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

Input = Entry()
Input.grid(column=2, row=1)

my_label = Label(text="Miles", font=("Arial", 10, "bold"))
my_label.grid(column=3, row=1)

equal = Label(text="is equal to", font=("Arial", 10, "bold"))
equal.grid(column=1, row=2)

equal_to_kilo = Label(text="0", font=("Arial", 10, "bold"))
equal_to_kilo.grid(column=2, row=2)

kilo = Label(text="Kilo", font=("Arial", 10, "bold"))
kilo.grid(column=3, row=2)


def btn_function():
    value = float(Input.get())
    con = Convert(value)
    equal_to_kilo.config(text=f"{con.convert()}")


btn = Button(text="Calculate", command=btn_function)
btn.grid(column=2, row=3)


window.mainloop()