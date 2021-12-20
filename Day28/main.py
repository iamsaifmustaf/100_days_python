
from tkinter import *
import math
from tkinter import font
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text=f"0:00")
    timer_label.config(text="Timer", fg="black")

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps%8)

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    
    if reps % 2 != 0:
        count_down(work_sec)
        new_label = check_mark.cget("text") + "✔"
        check_mark.config(text=new_label)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg="black", font=(FONT_NAME, 35, "bold"),bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

check_mark = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"),bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
tomato_image = canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100,130,text = "00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(height=5,width=15,text="Start", command=start_timer, bg=GREEN)
start_button.grid(column=0, row=2)

reset_button = Button(height=5,width=15,text="Reset", command=reset_timer, bg=RED)
reset_button.grid(column=2, row=2)




window.mainloop()