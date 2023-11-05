from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    my_label.config(text="Timer")
    canvas.itemconfig(canvas_text, text="00:00")
    check.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 0:
        countdown(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    elif REPS % 8 == 0:
        countdown(long_break_sec)
        my_label.config(text="Break", fg=RED)
    else:
        countdown(work_sec)
        my_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    timer_min = math.floor(count/60)
    timer_sec = count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    canvas.itemconfig(canvas_text, text=f"{timer_min}:{timer_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        timer_start()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            mark += "✔"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO TIMER")
window.config(padx=80, pady=50, bg=YELLOW)

my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 108, image=tomato_img)
canvas_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


btn_start = Button(text="Start", command=timer_start)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", command=timer_reset)
btn_reset.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check.grid(column=1, row=3)

window.mainloop()