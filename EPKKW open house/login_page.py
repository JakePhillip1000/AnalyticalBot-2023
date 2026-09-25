import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def exit():
    app.destroy()

# Login function
def login():
    entered_username = Username.get()
    entered_password = Pass.get()

# IF the name is Admin and password is 1234, then the login is success
    if entered_username == "Admin" and entered_password == "1234":
        exit()
         
        # Then it will transfer to the menu page
        import Menu_page
        Menu_page()
        
    # If password not correct, it will show the alert messagebox
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Creating a tkinter app and frame
app = tk.Tk()
app.geometry("900x640")
app.title("Login page")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = int(screen_width * 1.5)
window_height = int(screen_height * 1.5)

# Making the window width and height fit the frame
app.geometry(f"{window_width}x{window_height}")
app.attributes("-fullscreen", True)

img1 = ImageTk.PhotoImage(Image.open("img/Bluebackgroundv2.jpg"))
Bg = tk.Label(master=app, image=img1)
Bg.pack()

frame = tk.Frame(master=Bg, width=380, height=345, background="#051251")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

Acc = tk.Label(master=frame, text="Login into your Account", font=("Comic Sans MS", 20, "bold"), foreground= "#FFFFFF", background="#051251")
Acc.place(x=40, y=45)

user = tk.Label(frame, text = "Username: ")
user.configure(font=("Comic Sans MS", 12, "bold"), background= "#051251", foreground="#FFFFFF")
user.place(x=20, y=105)

Username = tk.Entry(master=frame, width=25, font=("Comic Sans MS", 12, "bold"), bd=2, background= "#005599", foreground="white")
Username.place(x=110, y=110)

password = tk.Label(frame, text = "Password: ")
password.configure(font=("Comic Sans MS", 12, "bold"), background= "#051251", foreground="#FFFFFF")
password.place(x=20, y=145)

Pass = tk.Entry(master=frame, width=25, font=("Comic Sans MS", 12, "bold"), bd=2, show="*", background="#005599", foreground="White")
Pass.place(x=110, y=150)

forgot = tk.Label(master=frame, text="Forgot your password", font=("Comic Sans MS", 12, "bold"), background= "#051251", foreground="#FFFFFF")
forgot.place(x=175, y=180)

button1 = tk.Button(master=frame, width=15, text="Login", font=("Comic Sans MS", 12, "bold"), foreground="white", background="#C000E6", command=login)
button1.place(x=110, y=220)

img2 = Image.open("img/Google.png").resize((20, 20))
img2 = ImageTk.PhotoImage(img2)
img3 = Image.open("img/instagram3.png").resize((20, 20))
img3 = ImageTk.PhotoImage(img3)

button2 = tk.Button(master=frame, image=img2, text="Google", width=100, height=28, compound="left", font=("Comic Sans MS", 12), background= "White", foreground="Black" )
button2.place(x=50, y=280)

button3 = tk.Button(master=frame, image=img3, text="instagram", width=100, height=28, compound="left", font=("Comic Sans MS", 12), background= "White", foreground="Black")
button3.place(x=225, y=280)

buttonexits = tk.Button(app, font=("Comic Sans MS", 12, "bold"), text="X", width=10, height=1, command=exit, background="red", foreground="White")
buttonexits.place(x=1423, y=0)

app.mainloop()
