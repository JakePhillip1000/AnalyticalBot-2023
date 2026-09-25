import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exit():
    root.destroy()

# Clearing the error text
def clear_error_label():
    error_label.config(text="")

# Function that create a matplotlib graph
def create_graph():
    x_values = x_entry.get().split(",")
    y_values = y_entry.get().split(",")

# When number of values x and y not equal, it will show the error text
    if len(x_values) != len(y_values):
        error_label.config(text="ERROR VALUE, please try again")
        root.after(4000, clear_error_label) 
        return

    try:
        x_values = list(map(str, x_values))
        y_values = list(map(int, y_values))
    except ValueError:
        error_label.config(text="ERROR VALUE, please try again")
        root.after(4000, clear_error_label)  
        return

    # Getting the title for the entrybox
    title = title_entry.get()

    fig = plt.figure(figsize=(6, 4), dpi=100)
    plt.bar(x_values, y_values, color=["magenta", "#A200FF","#E93ADE", "#E93A9D", "#FBD459", "orange", "#CC4B42", "#3D99AC", "#3DAC54"])
    plt.title(title, color="#3D168E", font="Comic Sans MS", size="16")
    plt.xlabel("X values", color="#3D168E", font="Comic Sans MS", size=12)
    plt.ylabel("Y values", color="#3D168E", font="Comic Sans MS", size=12)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Creating the tkinter
root = tk.Tk()
root.title("Bar Graph Creator")
root.geometry("900x640")
root.config(background="Cyan")
root.option_add("font", "tahoma 14 bold")
root.attributes('-fullscreen', True)

title_label = tk.Label(root, text="The graph title:", background="lightgray", font=("Comic Sans MS", 16, "bold"))
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
title_entry = tk.Entry(root, font=("Arial", 14), foreground="blue")
title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

x_label = tk.Label(root, text="Input x values:", background="lightgray", font=("Comic Sans MS", 16, "bold"))
x_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
x_entry = tk.Entry(root, font=("Arial", 14), foreground="blue")
x_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

y_label = tk.Label(root, text="Input y values:", background="lightgray", font=("Comic Sans MS", 16, "bold"))
y_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
y_entry = tk.Entry(root, font=("Arial", 14), foreground="blue")
y_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

submit_button = tk.Button(root, text="Submit", background="Orange", foreground="white", font=("Comic Sans MS", 14, "bold"), command=create_graph)
submit_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

error_label = tk.Label(root, text="", font=("Comic Sans MS", 40, "bold"), background="#76F4C0", foreground="red")
error_label.place(x=500, y=700)

buttonexits = tk.Button(root, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command=exit, background="red", foreground="White")
buttonexits.place(x=1423, y=0)

error_label = tk.Label(root, text="", font=("Comic Sans MS", 40, "bold"), background="Cyan", foreground="red")
error_label.place(x=520, y=650)

root.mainloop()
