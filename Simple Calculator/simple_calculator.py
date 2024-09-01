import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percentage():
    try:
        result = eval(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square():
    try:
        result = eval(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_negative():
    current = entry.get()
    if current and current[0] == '-':
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[1:])
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, '-' + current)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the display entry widget
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout including Clear, Percentage, Square, and Negative buttons
buttons = [
    ('C', 'red'), ('%', 'lightgray'), ('√', 'lightgray'), ('/', 'lightgray'),
    ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('*', 'lightgray'),
    ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('-', 'lightgray'),
    ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('+', 'lightgray'),
    ('(-)', 'lightgray'), ('0', 'lightblue'), ('.', 'lightgray'), ('=', 'lightgray')
]

# Button size configuration
button_width = 5
button_height = 2
button_font = ('Arial', 18)

# Create and place the buttons
row_val = 1
col_val = 0
for button, color in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=clear_entry)
    elif button == '%':
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=percentage)
    elif button == '√':
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=square)
    elif button == '(-)':
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=toggle_negative)
    else:
        btn = tk.Button(root, text=button, width=button_width, height=button_height, font=button_font, bg=color, command=lambda b=button: click_button(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI event loop
root.mainloop()
