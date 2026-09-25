import tkinter as tk
import math

def exit():
    root.destroy()

# When clicking a button, it will display number on the calculator
def button_click(number):
    
    # This will get the value from the button that you press
    current = display.get()
    display.delete(0, tk.END)
    
    # Displaying the value on the screen
    display.insert(tk.END, current + str(number))

# For AC button, clearing all the values
def button_clear():
    display.delete(0, tk.END)

# For equal button, this will evaluate the value when click
def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR value")

# Creating a tkinter frame
root = tk.Tk()
root.geometry("450x700")
root.title("Advance calculator")
root.config(background="Black")
window_height = 640
window_width = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# For the display screen
display = tk.Entry(root, font=("Commic Sans MS", 30, "bold"), justify="left")
display.config(background="#FFD6A0", foreground="Black", width=15)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(30,10))

# Buttons 1-9, + - 8 / in the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("00", 4, 1), (".", 4, 2), ("+", 4, 3)
]

# Display the buttons
for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, font=("Comic Sans MS", 14, "bold"), padx=28, pady=28, background="#FFA914", foreground="black", anchor="center")
    button.grid(row=row, column=col, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)
    button.configure(command=lambda text=button_text: button_click(text), height=1, anchor="center")

# AC button displaying
clear_button = tk.Button(root, text="AC", font=("Comic Sans MS", 14, "bold"), padx=28, pady=28, command=button_clear, background="#FFA914", foreground="black")
clear_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

equal_button = tk.Button(root, text="=", font=("Comic Sans MS", 14, "bold"), padx=28, pady=28, command=button_equal, background="#FFA914", foreground="black")
equal_button.grid(row=5, column=1, columnspan=1, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

buttonexits = tk.Button(root, font=("Comic Sans MS", 10, "bold"), text="X", width=5, height=1, command = exit, background="red", foreground="White")
buttonexits.place(x = 400, y = 0)

root.mainloop()
