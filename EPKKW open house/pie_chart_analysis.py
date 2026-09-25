import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def quit():
    window.destroy()

window = tk.Tk()
window.title("Pie chart creator")
window.geometry("900x640")
window.config(background="cyan")
window.option_add("font", "tahoma 10 bold")
window.attributes('-fullscreen', True)

def clear_error_label():
    error_label.config(text="")
    
# Creating a pie chart
def generate_pie_chart():
    values = entry_values.get()
    values = values.split(',')
    
    legends = entry_legends.get()
    legends = legends.split(',')

# If number of x and y are not equal, it will shows an error
    if len(values) != len(legends):
        error_label.config(text="ERROR VALUE, please try again")
        window.after(4000, clear_error_label)
        return

    try:
        values = [float(val) for val in values]
    except ValueError:
        error_label.config(text="ERROR VALUE, please try again")
        window.after(4000, clear_error_label)
        return
    
    # Plotting a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=legends, autopct="%1.1f%%", shadow=True)
    ax.set_title(entry_title.get())

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=250)

# Title
label_title = tk.Label(window, text="Title:", font=("Verdana", 14, "bold"), background="lightgray")
label_title.place(x=50, y=50) 

entry_title = tk.Entry(window, font=("Verdana", 16), width=20)
entry_title.place(x=200, y=50) 

label_values = tk.Label(window, text="Input values", font=("Verdana", 14, "bold"), background="lightgray")
label_values.place(x=50, y=100)

# Values 
entry_values = tk.Entry(window, font=("Verdana", 14), width=22)
entry_values.place (x=200, y=100)

# Legends
label_legends = tk.Label(window, text="Legends:", font=("Verdana", 14, "bold"), background="lightgray")
label_legends.place(x=50, y=150)

entry_legends = tk.Entry(window, font=("Verdana", 16))
entry_legends.place(x=200, y=150)

# Submit button
button_submit = tk.Button(window, text="Submit", font=("Verdana", 16, "bold"), background="orange", foreground="white", command=generate_pie_chart)
button_submit.place(x=400, y=200)

# Exit button
buttonexits = tk.Button(window, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command = quit, background="red", foreground="White")
buttonexits.place(x=1423, y=0)

# When the value is error, it will shows this text error text
error_label = tk.Label(window, text="", font=("Comic Sans MS", 20, "bold"), background="cyan", foreground="red")
error_label.place(x=520, y=740)


window.mainloop()
