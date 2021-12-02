from tkinter import *

#initialize tkinter instance
window = Tk()
#set title
window.title("Challenge")
#minimum size window
window.minsize(width=200, height=200)
window.config(padx=20, pady=50)

#Create labels
miles_desc_label = Label(text="Miles")
km_desc_label = Label(text="Km")
km_num_label = Label(text="0")
comment_label = Label(text="is equal to")

#Create Entries
entry_field = Entry(width=15)

#Placing Widgets on grid
miles_desc_label.grid(column=2, row=0)
km_desc_label.grid(column=2, row=1)
km_num_label.grid(column=1, row=1)
comment_label.grid(column=0, row=1)
entry_field.grid(column=1, row=0)

#Create Button and Button function
def calculate():
    num = int(entry_field.get()) * 1.609344
    km_num_label.config(text=round(num,2)) 

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()