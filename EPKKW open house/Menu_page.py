# Import the nessary libraries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
import re
import os
import math
import fractions

def CSV_graph():
    import Tkinter_CSV

def calculator():
    import Calculator
    
def bargraph():
    import Bar_graph_analysis
    
def piechart():
    import pie_chart_analysis
    
def scatterplot():
    import Scatter_plot_analysis
    
def linechart():
    import Line_chart_analysis
    
def chatbot():
    import CoconutZChatBot
    
def exit():
    app.destroy()

def withdraw():
    app.withdraw()

app = tk.Tk()
app.title("Menu page")
app.geometry("900x640")
app.config(background = "#061E6A")
app.attributes('-fullscreen', True)

# Bot picture
image_path = "img/coconut.png"
image = Image.open(image_path)
image = image.resize((60, 60))
photo = ImageTk.PhotoImage(image)

# User picture
image_path1 = "img/user.png"
image1 = Image.open(image_path1)
image1 = image1.resize((60, 60))
photo1 = ImageTk.PhotoImage(image1)

Title = tk.Label(app, text = "Analytical Bot")
Title.configure(font=("Courier New", 50, "bold"), background= "#061E6A", foreground="#F6A6FD")
Title.place(x=40, y=150)

Title = tk.Label(app, text = "(Experimental version)")
Title.configure(font=("Courier New", 20, "bold"), background= "#061E6A", foreground="#F6A6FD")
Title.place(x=105, y=225)

Text = Title = tk.Label(app, text = " ◉ Chatbot and calculator mode")
Title.configure(font=("Comic Sans MS", 20, "bold"), background= "#061E6A", foreground="#A6F4FD")
Title.place(x=40, y=300)

button1 = tk.Button(app, text="Chatbot", width=15, height=1, command = chatbot)
button1.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button1.place(x=100, y=350)

button2 = tk.Button(app, text="Calculator", width=15, height=1, command = calculator)
button2.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button2.place(x=100, y=420)

paragraph = tk.Label(app, text = " ◉ Data analysis mode")
paragraph.configure(font=("Comic Sans MS", 20, "bold"), background= "#061E6A", foreground="#A6F4FD")
paragraph.place(x=40, y=520)

button3 = tk.Button(app, text="Bar graph", width=15, height=1, command = bargraph)
button3.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button3.place(x=100, y=570)

button4 = tk.Button(app, text="Pie chart", width=15, height=1, command = piechart)
button4.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button4.place(x=100, y=640)

button5 = tk.Button(app, text="Scatter plot", width=15, height=1, command = scatterplot)
button5.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button5.place(x=350, y=570)

button6 = tk.Button(app, text="Line graph", width=15, height=1, command = linechart)
button6.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button6.place(x=350, y=640)

button7 = tk.Button(app, text="AnalystCX (CSV files)", width=30, height=1, command = CSV_graph)
button7.configure(font=("Comic Sans MS", 18, "bold"), background="Black", foreground="#A6F4FD")
button7.place(x=115, y=710)

buttonexits = tk.Button(app, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command = exit, background="red", foreground="White")
buttonexits.place(x=1423, y=0)

app.mainloop()
