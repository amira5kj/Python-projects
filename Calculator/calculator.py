import tkinter as tk

calculation="" #holds the current expression as a string
# the calculator part
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol) #"5" → "5+3"
    text_result.delete(1.0,"end") 
    text_result.insert(1.0,calculation)#Then updates UI

    

def evaluate_calculation():
#eval function > is a python functions that evalute python statement wheather its python code or numeric calculation
    global calculation
    try: #catch any errors that might occure
        calculation=str(eval(calculation)) #eval() computes the result when = is pressed
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")


def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")


# the GUI part 
root=tk.Tk() #create the object "the window that is called root "

for i in range(7):  # rows (0 to 6)
    root.grid_rowconfigure(i, weight=1)

for j in range(5):  # columns (0 to 4)
    root.grid_columnconfigure(j, weight=1)
#root.geometry("350x400") #fixed static size
root.resizable(True, True)

text_result = tk.Text(root, height=3, width=19, font=("Arial",24))
text_result.grid(columnspan=5, sticky="nsew")
 

numbers = [  #(number,row,column)
    (1,2,1),(2,2,2),(3,2,3),("+", 2, 4),
    (4,3,1),(5,3,2),(6,3,3),("-", 3, 4),
    (7,4,1),(8,4,2),(9,4,3),("*", 4, 4),
    ("(",5,1),(0,5,2),(")",5,3),("/", 5, 4)
]

for num, r, c in numbers:
    tk.Button(
        root,
        text=str(num),
        command=lambda n=num: add_to_calculation(n),
        width=5,
        font=("Arial", 15)
    ).grid(row=r, column=c,sticky="nsew")

special_buttons = [
    ("=", evaluate_calculation, 6, 1, 2),  # (text, command, row, col, colspan)
    ("C", clear_field, 6, 3, 2),
]

for text, cmd, r, c, span in special_buttons:
    tk.Button(
        root,
        text=text,
        command=cmd,
        width=5,
        font=("Arial", 15)
    ).grid(row=r, column=c, columnspan=span, sticky="nsew")

root.mainloop() 
