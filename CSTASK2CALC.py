CSTASK2CALC
import tkinter as tk

def calculations():
    try:
        result = eval(entry.get())
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

 
root = tk.Tk()
root.title("Calculator")
 
entry = tk.Entry(root)
entry.pack()

 
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0

for button in buttons:
    tk.Button(button_frame, text=button, command=lambda b=button: entry.insert('end', b)
              if b != '=' else evaluate_expression()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

 
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
