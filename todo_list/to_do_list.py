from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Ethan's to-do List")
root.geometry("450x550")

def newTask():
    task = my_entry.get()
    if task  != "":
        task_box.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

root.bind("<Return>", newTask)

def deleteTask():
    task_box.delete(ANCHOR)

frame = LabelFrame(
    root,
    text = "What needs to be done today?",
    bg = "#f0f0f0",
    font = 20
)
frame.pack(expand = TRUE, fill = BOTH, pady = 10)

task_box = Listbox(
    frame,
    width = 30,
    height = 10,
    font = ("Calibri", 16),
    bd = 1,
    fg = "#63B8FF",
    highlightthickness = 0,
    activestyle = None,
)
task_box.pack(side = LEFT, fill =  BOTH)


sb = Scrollbar(frame)
sb.pack(side = RIGHT, fill = BOTH)

task_box.config(yscrollcommand = sb.set)
sb.config(command = task_box.yview)

my_entry = Entry(
    root,
    font = ("calibri", 16)
)
my_entry.pack(pady = 20)

button_frame = Frame(root)
button_frame.pack(pady = 20)

addtaskbutton = Button(
    button_frame,
    text = "Add",
    font = ("calibri 12"),
    fg = "green",
    padx = 10,
    pady = 5,
    command = newTask
)
addtaskbutton.pack(fill = BOTH, expand = TRUE, side = LEFT)

deleteTask_button = Button(
    button_frame,
    text = "Delete Task",
    font = ("calibri 12"),
    fg = "red",
    padx = 10,
    pady = 5,
    command = deleteTask
)
deleteTask_button.pack(fill = BOTH, expand = TRUE, side = LEFT)

root.mainloop()