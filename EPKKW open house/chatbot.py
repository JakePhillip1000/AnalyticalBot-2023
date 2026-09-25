# Import necessary libaries
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
import re
import random
import math

def quit():
    app.destroy()

# Math function, this will be use when we type math question
def evaluate_math_expression(expression):
    try:
        # fractions
        expression = re.sub(r"([^\d)])\s*/\s*([^\d(])", r"\1/\2", expression)
        expression = expression.replace("/", "+fractions.Fraction(")
        
        # factorial
        expression = expression.replace("!", "math.factorial")

        # log function (base 10)
        expression = expression.replace("log", "math.log10")
        
        # trigonometric functions
        trig_functions = ["sin", "cos", "tan"]
        for function in trig_functions:
            while f"{function}(" in expression:
                match = re.search(rf"{function}\((\d+)\)", expression)
                if match:
                    angle_degrees = int(match.group(1))
                    angle_radians = math.radians(angle_degrees)

                    if function == "sin":
                        trig_value = math.sin(angle_radians)
                    elif function == "cos":
                        trig_value = math.cos(angle_radians)
                    elif function == "tan":
                        trig_value = math.tan(angle_radians)

                    expression = expression.replace(match.group(0), str(trig_value))

        #  square root
        expression = expression.replace("sqrt", "math.sqrt")

        result = eval(expression)
        return str(result)
    except Exception:
        return None

def is_calculation_expression(expression):
    # Check if the expression contains any mathematical operators (+, -, *, /, **)
    return re.search(r"[-+*/**=]", expression)

def key(question):
    question = question.lower()
    
    if "what" in question:
        expression = question.replace("what", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "=" in question:
        expression = question.replace("=", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "how" in question:
        expression = question.replace("how", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "calculate" in question:
        expression = question.replace("calculate", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "evaluate" in question:
        expression = question.replace("evaluate", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."

    if "what is" in question:
        expression = question.replace("what is", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."

    if "what are" in question:
        expression = question.replace("what are", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "please calculate" in question:
        expression = question.replace("please calculate", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
    if "show" in question:
        expression = question.replace("show", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return  "Coconutz(Bot): Sorry, I couldn't evaluate the expression." 
    
    if "please explain" in question:
        expression = question.replace("please explain", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot):Sorry, I couldn't evaluate the expression."
        
    if "explain" in question:
        expression = question.replace("explain", "").strip()
        result = evaluate_math_expression(expression)
        if result is not None:
            return "Coconutz(Bot): The result is: " + result
        else:
            return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."
        
def key(question):
    expression = re.search(r"([a-z]+)\((\d+)\)\s*([+\-*/])\s*([a-z]+)\((\d+)\)", question)
    if expression:
        function1 = expression.group(1)
        angle1_degrees = int(expression.group(2))
        angle1_radians = math.radians(angle1_degrees)
        
        operator = expression.group(3)
        
        function2 = expression.group(4)
        angle2_degrees = int(expression.group(5))
        angle2_radians = math.radians(angle2_degrees)
        
        if function1 in ["sin", "cos", "tan"] and function2 in ["sin", "cos", "tan"]:
            trig_value1 = math.sin(angle1_radians) if function1 == "sin" else (
                math.cos(angle1_radians) if function1 == "cos" else math.tan(angle1_radians)
            )
            
            trig_value2 = math.sin(angle2_radians) if function2 == "sin" else (
                math.cos(angle2_radians) if function2 == "cos" else math.tan(angle2_radians)
            )
            
            if operator == "+":
                result = trig_value1 + trig_value2
            elif operator == "-":
                result = trig_value1 - trig_value2
            elif operator == "*":
                result = trig_value1 * trig_value2
            elif operator == "/":
                result = trig_value1 / trig_value2
                
            response = f"Coconutz(Bot): {function1}({angle1_degrees} degrees) {operator} {function2}({angle2_degrees} degrees) = {result}"
            return response
        
    keywords = ["what is", "what are", "please calculate", "show", "please explain", "explain", "=", "sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "!", "evaluate", "what", "explain", "how", "showing that", "calculate", "how is"]
    question = question.lower()
        
      # Typing or mispelled the word, the bot can still calculate + make the keywords work when calculating numbers
    for key in question:
        if key in question:
            expression = re.search(rf"(?:.*?\b{re.escape(key)}\b\s*)(\d+\s*(?:[-+*/]\s*\d+\s*)+)", question)
            if expression:
                result = evaluate_math_expression(expression.group(1))
                if result is not None:
                    return f"Coconutz(Bot): The result is: {result}"
                else:
                    return "Coconutz(Bot): Sorry, I couldn't evaluate the expression."

# When submitting the question, this will make the bot use find the answer, can be either mathematic or information
def submit():
    button.config(background="#C90400")
    user_input = entry1.get().strip()
    if user_input:
        old_chat.append("User: " + user_input)

        response = key(user_input)
        if response is None:
            result = evaluate_math_expression(user_input)
            if result is not None:
                response = "Coconutz(Bot): " + result
            else:
                result = google_search(user_input)
                if result:
                    response = "Coconutz(Bot): " + result["text"] 
                else:
                    response = "Coconutz(Bot): Sorry, I don't have information on this."

        old_chat.append(response)
        update_chat()
        entry1.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "Please type something before you submit")

def update_chat():
    chat_display.config(state=tk.NORMAL)
    chat_display.delete(1.0, tk.END)

    # Displaying the coconut picture infront of the bot
    for chat_entry in old_chat:
        if chat_entry.startswith("Coconutz(Bot): "):
            chat_display.image_create(tk.END, image=photo)
    
    # Displaying the user picture infront of the user
        elif chat_entry.startswith("User: "):
            chat_display.image_create(tk.END, image=photo1)
            
        chat_display.insert(tk.END, chat_entry + "\n\n")

    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def on_enter(event):
    submit()

# Scrollbar function
def update_scrollbar(event):
    chat_display.yview_moveto(1.0)
    chat_display.update_idletasks()

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

# The google search function
def scrape_google(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.th/search?q=" + query)

    links = list(response.html.absolute_links)
    google_app = ('https://www.google.',
                  'https://google.',
                  'https://webcache.googleusercontent.',
                  'http://webcache.googleusercontent.',
                  'https://policies.google.',
                  'https://support.google.',
                  'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_app):
            links.remove(url)

    return links

def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.th/search?q=" + query)
    return response

def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    if results:
        result = results[0]
        item = {
            "title": result.find(css_identifier_title, first=True).text,
            "link": result.find(css_identifier_link, first=True).attrs["href"],
            "text": result.find(css_identifier_text, first=True).text
        }
        return item
    else:
        return None

# When there is information in the Google
def google_search(query):
    try:
        response = get_results(query)
        result = parse_results(response)

# When there is no information in Google
        if result:
            return result
        else:
            print("Coconutz(Bot): I don't understand the question")
            return None
    except:
        print("Coconutz(Bot): Sorry, I don't have information on this.")

app = tk.Tk()
app.title("Chatbot")
app.attributes("-fullscreen", True)
app.config(background="#00052E")

# Create a frame
frame = tk.Frame(app, background="#261F8C", width=1080, height=670)
frame.pack(expand=True, fill=tk.BOTH)
frame.place(x=410, y=0)

frame2 = tk.Frame(app, background="#005194", width=345, height=870)
frame2.place(x=30, y=0)

frame3 = tk.Frame(app, background="#090041", width=1080, height=225)
frame3.place(x=410, y=649)

# The chatbot title
Title = tk.Label(frame2, text="CHATBOT")
Title.configure(font=("Comic Sans MS", 35, "bold"), background="#005194", foreground="#FDCFFF")
Title.place(x=60, y=35)

Title2 = tk.Label(frame2, text="(experimental version 1.0)")
Title2.configure(font=("Courier New", 15, "bold"), background="#005194", foreground="#FDCFFF")
Title2.place(x=17, y=100)

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

# The entry box
message1 = tk.Label(frame3, text="Send a message: ")
message1.configure(font=("Comic Sans MS", 18, "bold"), background="#000048", foreground="#FDCFFF")
message1.place(x=20, y=68)

entry1 = tk.Entry(app, width=30, font=("Comic Sans MS", 25, "bold"), background="#00569F", foreground="White")
entry1.config(width=32)
entry1.place(x=640, y=715)
entry1.bind("<Return>", on_enter)
entry1.bind("<KeyRelease>", update_scrollbar) 

# Exit button
buttonexits = tk.Button(app, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command = quit, background="#D30000", foreground="White")
buttonexits.place(x=1360, y=0)

# Sending button
button = tk.Button(frame3, text="Submit", command=submit, font=("Comic Sans MS", 15, "bold"), background="#FF7900", foreground="white")
button.config()
button.place(x=890, y=65)

# Displaying the response from you
old_chat = []
chat_display = tk.Text(frame, font=("Comic Sans MS", 20, "bold"), wrap=tk.WORD, width=66, height=17, background="#261F8C", foreground="White")
chat_display.place(x=0, y=0)     

# Scrollbar for the chat display
chat_scrollbar = tk.Scrollbar(frame, command=chat_display.yview,)
chat_scrollbar.place(x=1060, y=0, height=650, width=20)
chat_display.config(yscrollcommand=chat_scrollbar.set)
chat_display.bind("<Configure>", update_scrollbar)

app.mainloop()