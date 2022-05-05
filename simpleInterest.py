import re
from sqlite3 import InternalError
from time import time
from tkinter import *
from unittest import result

window = Tk()
window.title('Simple Interest Calculator')
window.geometry("300x500")
window.configure(bg="#D6E5FA")

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest=round(i, 2)
    output.destroy()
    result = Label(output_frame, text="Final Interest calculated is Rs."+str(interest), bg="#D6E5FA", font="Helvetica 10", width=30)
    result.place(x=20, y=40)
    result.pack()

heading = Label(window, text="Simple Interest Calculator", fg="black", bg="#D6E5FA", font="Helvetica 13 bold")
heading.place(x=43, y=10)

principle_L=Label(window, text="Principle", fg = "black", bg = "#D6E5FA", font="Helvetica",bd=1)
principle_L.place(x=20, y=90)
principle=Entry(window, text="", bd=2, width=22, bg="#FFF9F9")
principle.place(x=130, y=92)

rate_L = Label(window, text="Rate", fg="black", bg="#D6E5FA", font="Helvetica",bd=1)
rate_L.place(x=20, y=140)
rate=Entry(window, text="", bd=2, width=22, bg="#FFF9F9")
rate.place(x=130, y=142)

time_L = Label(window, text="Time", fg="black", bg="#D6E5FA", font="Helvetica",bd=1)
time_L.place(x=20, y=190)
time=Entry(window, text="", bd=2, width=22, bg="#FFF9F9")
time.place(x=130, y=192)

calculate = Button(window, text="Calculate", bg="#D6E5FA", fg="black", bd=4, width=20, command=calculate_interest)
calculate.place(x=70, y=250)

output_frame = LabelFrame(window, text="Result", bg="#D6E5FA", font= "Helvetica")
output_frame.pack(padx=20, pady=20)
output_frame.place(x=10, y=310)
output = Label(output_frame, text="Your result will be displayed here!", bg="#D6E5FA", font="Helvetica 10", width=34)
output.place(x=20, y=20)
output.pack()

window.mainloop()