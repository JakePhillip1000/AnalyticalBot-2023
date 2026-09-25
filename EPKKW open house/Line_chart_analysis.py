import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def exit():
    root.destroy()

root = tk.Tk()
root.title("Line graph Creator")
root.geometry("900x640")
root.config(background="#00C45D")
root.attributes('-fullscreen', True)

def create_graph():
    x_values = x_entry.get().split(",")
    y_values = y_entry.get().split(",")

def clear_error_label():
    error_label.config(text="")

def create_graph():
    x_values = x_entry.get().split(",")
    y_values = y_entry.get().split(",")

    if len(x_values) != len(y_values):
        error_label.config(text="ERROR VALUE, please try again")
        root.after(4000, clear_error_label) 
        return
    
    try:
        x_values = list(map(int, x_values))
        y_values = list(map(int, y_values))
    except ValueError:
        error_label.config(text="ERROR VALUE, please try again")
        root.after(4000, clear_error_label)  
        return

    # Get the title
    title = title_entry.get()

    fig = plt.figure(figsize=(6, 4), dpi=100)
    plt.plot(x_values, y_values, color="Purple", linestyle = "-", marker = "o")
    plt.title(title, color="Green", font="Verdana", size=16, fontweight = "bold")
    plt.xlabel("X values", color="Black", font="Verdana", size=12)
    plt.ylabel("Y values", color="Black", font="Verdana", size=12)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10)

title_label = tk.Label(root, text="The graph title:", background="lightgray", font=("Verdana", 16))
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
title_entry = tk.Entry(root, font=("tahoma", 14))
title_entry.config(width=22, background="Turquoise", foreground="Blue")
title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

x_label = tk.Label(root, text="Input x values:", background="lightgray", font=("Verdana", 16))
x_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
x_entry = tk.Entry(root, font=("Arial", 14))
x_entry.config(background="Turquoise", foreground="Blue")
x_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

y_label = tk.Label(root, text="Input y values:", background="lightgray", font=("Verdana", 16))
y_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
y_entry = tk.Entry(root, font=("Arial", 14))
y_entry.config(background="Turquoise", foreground="Blue")
y_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

submit_button = tk.Button(root, text="Submit", background="Orange", foreground="white", font=("tahoma", 14, "bold"), command=create_graph)
submit_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

error_label = tk.Label(root, text="", font=("Comic Sans MS", 20, "bold"), background="#00C45D", foreground="#890600")
error_label.place(x=520, y=630)

buttonexits = tk.Button(root, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command = exit, background="red", foreground="White")
buttonexits.place(x=1423, y=0)

root.mainloop()