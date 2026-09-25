import tkinter as tk
import tkinter as ttk
from tkinter import messagebox

app = tk.Tk()
app.title("Chatbot Setting")
app.geometry("600x600")
# app.attributes("-fullscreen", True)
app.config(background="#2A0061")

def exitting():
    app.destroy()

# Title and background
Setting_title = tk.Label(app, text="Setting")
Setting_title.configure(font=("Comic Sans MS", 40, "bold"), background="#2A0061", foreground="#FF5353")
Setting_title.place(x=40, y=10)

bg = tk.Label(app, text="Background → ")
bg.configure(font=("Comic Sans MS", 15, "bold"), background="#2A0061", foreground="#FF8686")
bg.place(x=40, y=130)

blue = tk.Label(app, text="blue")
blue .configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#48A6FF")
blue.place(x=250, y=90)

blue_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#48A6FF")
blue_color.place(x=240, y=130)

green = tk.Label(app, text="green")
green.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#0EB800")
green.place(x=335, y=90)

green_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#0EB800")
green_color.place(x=330, y=130)

red = tk.Label(app, text="red")
red.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="red")
red.place(x=430, y=90)

red_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="red")
red_color.place(x=420, y=130)

black = tk.Label(app, text="Black")
black.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#060606")
black.place(x=515, y=90)

black_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="black")
black_color.place(x=510, y=130)

violet = tk.Label(app, text="violet")
violet.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#C800CB")
violet.place(x=245, y=180)

violet_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#C800CB")
violet_color.place(x=238, y=210)

gray = tk.Label(app, text="gray")
gray.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#878787")
gray.place(x=340, y=180)

gray_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#878787")
gray_color.place(x=330, y=210)

white = tk.Label(app, text="white")
white.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="White")
white.place(x=425, y=180)

white_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="white")
white_color.place(x=420, y=210)

orange = tk.Label(app, text="orange")
orange.configure(font=("Comic Sans MS", 12, "bold"), background="#2A0061", foreground="#FF7400")
orange.place(x=510, y=180)

orange_color = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#FF7400")
orange_color.place(x=510, y=210)

# User log color
user_log= tk.Label(app, text="User Log → ")
user_log.configure(font=("Comic Sans MS", 15, "bold"), background="#2A0061", foreground="#FF8686")
user_log.place(x=40, y=300)

user_green = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#0EB800")
user_green.place(x=235, y=300)

user_purple = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#8500CB")
user_purple.place(x=330, y=300)

user_lightblue = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#00D4FF")
user_lightblue.place(x=420, y=300)

user_orange = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#FF7400")
user_orange.place(x=510, y=300)

# Bot log color
user_log= tk.Label(app, text="Bot Log → ")
user_log.configure(font=("Comic Sans MS", 15, "bold"), background="#2A0061", foreground="#FF8686")
user_log.place(x=40, y=370)

bot_green = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#0EB800")
bot_green.place(x=235, y=370)

bot_purple = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#8500CB")
bot_purple.place(x=330, y=370)

bot_lightblue = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#00D4FF")
bot_lightblue.place(x=420, y=370)

bot_orange = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#FF7400")
bot_orange.place(x=510, y=370)

# Text User
text_user= tk.Label(app, text="Text User → ")
text_user.configure(font=("Comic Sans MS", 15, "bold"), background="#2A0061", foreground="#FF8686")
text_user.place(x=40, y=440)

text_user_green = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#0EB800")
text_user_green.place(x=235, y=440)

text_user_purple = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#8500CB")
text_user_purple.place(x=330, y=440)

text_user_lightblue = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#00D4FF")
text_user_lightblue.place(x=420, y=440)

text_user_orange = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#FF7400")
text_user_orange.place(x=510, y=440)

# Text bot
text_bot = tk.Label(app, text="Text Bot → ")
text_bot.configure(font=("Comic Sans MS", 15, "bold"), background="#2A0061", foreground="#FF8686")
text_bot.place(x=40, y=510)

text_bot_green = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#0EB800")
text_bot_green.place(x=235, y=510)
text_bot_purple = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#8500CB")
text_bot_purple.place(x=330, y=510)

text_bot_lightblue = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#00D4FF")
text_bot_lightblue.place(x=420, y=510)

text_bot_orange = tk.Button(app, font=("Comic Sans MS", 12, "bold"), width=5, height=1, background="#FF7400")
text_bot_orange.place(x=510, y=510)

# Exit button
buttonexits = tk.Button(app, font=("Comic Sans MS", 12, "bold"), text="X", width=5, height=1, command = exitting, background="#D30000", foreground="White")
buttonexits.place(x=540, y=0)

app.mainloop()
