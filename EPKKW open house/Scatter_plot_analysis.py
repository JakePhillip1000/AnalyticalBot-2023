import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random as rd

def exit():
    root.destroy()

root = tk.Tk()
root.title("Line graph Creator")
root.geometry("900x640")
root.config(background="#D6A3E2")
root.attributes('-fullscreen', True)

def create_graph():
    x_values = x_entry.get().split(",")
    y_values = y_entry.get().split(",")

def clear_error_label():
    error_label.config(text="")

def create_graph():
    x_values = x_entry.get().split(",")
    y_values = y_entry.get().split(",")

    # When number of x and y value are not equal, it wil shows the error text
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

    # Getting the title fropm what you write
    title = title_entry.get()
    
    # getting x and y values and plot them on graph
    fig = plt.figure(figsize=(6, 4), dpi=100)
    plt.scatter(x_values, y_values, linestyle = "-", marker = "o")
    plt.title(title, color="Violet", font="Comic Sans MS", size=16, fontweight = "bold")
    plt.xlabel("X values", color="Black", font="Comic Sans MS", size=12)
    plt.ylabel("Y values", color="Black", font="Comic Sans MS", size=12)
    
    # Displaying the graph
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10)

title_label = tk.Label(root, text="The graph title:", background="#D6A3E2", font=("Comic Sans MS", 16, "bold"))
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
title_entry = tk.Entry(root, font=("Comic Sans MS", 14, "bold"))
title_entry.config(width=20, background="cyan", foreground="Blue")
title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

x_label = tk.Label(root, text="Input x values:", font=("Comic Sans MS", 16, "bold"), background="#D6A3E2")
x_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
x_entry = tk.Entry(root, font=("Comic Sans MS", 14, "bold"))
x_entry.config(background="Lightgreen", foreground="Blue")
x_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

y_label = tk.Label(root, text="Input y values:", border=True, font=("Comic Sans MS", 16, "bold"),background="#D6A3E2")
y_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
y_entry = tk.Entry(root, font=("COmic Sans MS", 14, "bold"))
y_entry.config(background="Turquoise", foreground="Blue")
y_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

submit_button = tk.Button(root, text="Submit", background="orange", foreground="white", font=("Comic Sans MS", 14, "bold"), command=create_graph)
submit_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

buttonexits = tk.Button(root, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command = exit, background="red", foreground="White")
buttonexits.place(x=1425, y=0)

error_label = tk.Label(root, text="", font=("Comic Sans MS", 15, "bold"), background="#D6A3E2", foreground="red")
error_label.place(x=520, y=650)


root.mainloop()