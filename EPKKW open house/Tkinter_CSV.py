# Import libraries for using
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import statistics as st
import seaborn as sns
import pandas as pd

# Declare the none variable to the combobox to make selection process work
data = None
selected_column1 = None
selected_column2 = None
graph_created = False # Declare the graph variable as false making sure graph creation will not error
graph_canvas = None # Declare a variable that graph isn't create yet, it will be create soon

# Canvas for each graph, define them as none first
# TO determine whether they exists and can clear them when assigning new value
scatter_canvas = None
bar_canvas = None
pie_canvas = None
density_canvas = None
heatmap_canvas= None

def scatter():
    global data, selected_column1, selected_column2, scatter_canvas
    
    if selected_column1 and selected_column2:
        if scatter_canvas:
            scatter_canvas.get_tk_widget().destroy()
        
        # Clearing the frame    
        plt.clf()
        
        # frame size
        plt.figure(figsize=(6, 3.8))
        
        scatter_1 = {"family": "Comic Sans MS", "color": "#9E00DA", "fontsize": 14}
        plt.xlabel(selected_column1, fontdict=scatter_1)
        
        scatter_2 = {"family": "Comic Sans MS", "color": "#9E00DA", "fontsize": 14}
        plt.ylabel(selected_column2, fontdict=scatter_2)
        
        scatter_3= {"family": "Comic Sans MS", "color": "#004BBB", "fontsize": 16, "weight": "bold"}
        plt.title(f"{selected_column1} VS {selected_column2}", fontdict=scatter_3)
        
        # Selecting column that is being chosen from combobox
        plt.scatter(data[selected_column1], data[selected_column2], color="#FF5733", marker="o")
        
        # Creating a scatter chart canvas for displaying 
        scatter_canvas = FigureCanvasTkAgg(plt.gcf(), master=frame3)
        scatter_canvas.draw()
        scatter_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    else:
        messagebox.showwarning("ERROR!", "Please select x and y values.")

def bar():
    global data, selected_column1, selected_column2, bar_canvas

    if selected_column1 and selected_column2:
        if bar_canvas:
            bar_canvas.get_tk_widget().destroy()
            
        plt.clf()
        plt.figure(figsize=(6, 3.8))
        font = {"family": "Comic Sans MS", "color": "#9E00DA", "fontsize": 14}
        plt.xlabel(selected_column1, fontdict=font)
        
        font1 = {"family": "Comic Sans MS", "color": "#9E00DA", "fontsize": 14}
        plt.ylabel(selected_column2, fontdict=font1)
        
        font2 = {"family": "Comic Sans MS", "color": "#004BBB", "fontsize": 16, "weight": "bold"}
        plt.title(f"{selected_column1} VS {selected_column2}", fontdict=font2 )
        
        # Selecting column that is being chosen from combobox
        plt.bar(data[selected_column1], data[selected_column2], color=["magenta", "#A200FF","#E93ADE", "#E93A9D",\
            "#FBD459", "orange", "#CC4B42", "#3D99AC", "#3DAC54", "#5FFFF3", "#BD5FFF", "#5FFFC9", "#0036C8"])
        
        # Creating a bar graph canvas for displaying the bar graph
        bar_canvas = FigureCanvasTkAgg(plt.gcf(), master=frame1)
        bar_canvas.draw()
        bar_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    else:
        messagebox.showwarning("ERROR!", "Please select x and y values.") 
        
# Density plot
def density_plot():
    global data, selected_column1, density_canvas
    
    if data is not None and selected_column1:
        if density_canvas:
            density_canvas.get_tk_widget().destroy()
        
        plt.clf()
        fig1 = plt.figure(figsize=(6, 3.8))
        
        # The column x must be numeric in order to make a graph
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        if selected_column1 in numeric_columns:
            
            # Creating the density plot
            sns.kdeplot(data[selected_column1], shade=True, color="#047500", label=selected_column1, alpha=0.7)
            
            # Decorating the plot
            densityfont = {"family": "Comic Sans MS", "color": "#004BBB", "fontsize": 16, "weight": "bold"}
            plt.title(f"Density Plot of {selected_column1}", fontdict=densityfont)
            plt.legend()
            
            # Displaying the plot on the canvas
            density_canvas = FigureCanvasTkAgg(fig1, master=frame2)
            density_canvas.draw()
            density_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showwarning("ERROR!", "Column X must be numeric value")
        
    else:
        messagebox.showwarning("ERROR!", "Please select a value.")

# The heatmap chart
def heatmap():
    global data, selected_column1, selected_column2, heatmap_canvas
    
    if (data is not None) and (selected_column1 and selected_column2):
        if heatmap_canvas:
            heatmap_canvas.get_tk_widget().destroy()
        
        # Clearing the old graph when selecting new values    
        plt.clf()
        plt.figure(figsize=(6, 3.8))
        
        # Selecting only numeric columns for heatmap calculation
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        selected_columns = [selected_column1, selected_column2]
        valid_columns = [col for col in selected_columns if col in numeric_columns]

        # Both columns must be numeric
        if len(valid_columns) < 2:
            messagebox.showwarning("ERROR!", "Both columns must be numeric")
            return
        
        # Creating a heatmap 
        selected_data = data[valid_columns]
        sns.heatmap(selected_data.corr(), annot=True, cmap="coolwarm", center=0)
        
        heatmap_font = {"family": "Comic Sans MS", "color": "#004BBB", "fontsize": 16, "weight": "bold"}
        plt.title(f"{selected_column1} and {selected_column2}", fontdict=heatmap_font)
        
        # Creating a heatmap canvas for displaying 
        heatmap_canvas = FigureCanvasTkAgg(plt.gcf(), master=frame4)
        heatmap_canvas.draw()
        heatmap_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    else:
        messagebox.showwarning("ERROR!", "Please select x and y values")

def quit():
    app.destroy()
    
# creating a table-like display of the data in a frame 
def labels(data_frame, frame):
    # Displaying the CSV files chosen on the frame
    for col_index, col_name in enumerate(data_frame):
        label = tk.Label(frame, text=col_name, anchor="center", font=("Comic Sans MS", 12, "bold"), background="#350097", foreground="white")
        label.grid(row=0, column=col_index+1, padx=5, pady=5, sticky="ew")
    
    # Displaying the colum and rows
    for index, row in data_frame.iterrows():
        label = tk.Label(frame, text=str(index), anchor="center", font=("Comic Sans MS", 12), background="#350097", foreground="white")
        label.grid(row=index+1, column=0, padx=5, pady=5, sticky="ns")

        # Making the color vaires (different), even row = darker color
        for col_index, value in enumerate(row):
            cell_color = "#350097" if (index + col_index) % 2 == 0 else "#26006D"
            label = tk.Label(frame, text=str(value), anchor="center", font=("Comic Sans MS", 12), background=cell_color, foreground="white")
            label.grid(row=index+1, column=col_index+1, padx=5, pady=5, sticky="nsew")

# Browsing files from your computer
def open_csv(inner_frame):
    global data, selected_column1, selected_column2, scatter_canvas, bar_canvas
    
    # Clearing old data and canvases
    data = None
    selected_column1 = None
    selected_column2 = None
    if scatter_canvas:
        scatter_canvas.get_tk_widget().destroy()
    if bar_canvas:
        bar_canvas.get_tk_widget().destroy()
    
    # Clear the inner frame where CSV data is displayed inside the canvas
    for widget in inner_frame.winfo_children():
        widget.destroy()
    
    # Getting the file, browsing from your computer
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        combobox["values"] = data.columns.tolist()
        combobox1["values"] = data.columns.tolist()
        labels(data, inner_frame)

# Creating a dropdown box function for choosing the values to make a graph
# The combobox 1, x value (dropdownbox)
def drop_combobox(event):
    global data, selected_column1, inner_frame, combobox, graph_created
    current_column1 = combobox.get()
    
    if current_column1 and current_column1 != selected_column1:
        selected_column1 = current_column1
        graph_created = False
        
        # Destroying the old graph when selecting new value
        if scatter_canvas:
            scatter_canvas.get_tk_widget().destroy()
            
        if bar_canvas:
            bar_canvas.get_tk_widget().destroy()
            
        if density_canvas:
            density_canvas.get_tk_widget().destroy()
            
        if heatmap_canvas:
            heatmap_canvas.get_tk_widget().destroy()
            
    if selected_column1:
        inner_frame.destroy()
        inner_frame = tk.Frame(canvas, background="#350097")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        inner_frame.bind("<Configure>", lambda evt: canvas.configure(scrollregion=canvas.bbox("all")))
        labels(data[[selected_column1, selected_column2]], inner_frame)
    combobox.set(selected_column1)

# The combobox 1, y value (dropdownbox)
def drop_combobox1(event):
    global data, selected_column2, inner_frame, combobox1, graph_created
    current_column2 = combobox1.get()
    
    if current_column2 and current_column2 != selected_column2:
        selected_column2 = current_column2
        graph_created = False

        # Destroying the old graph when selecting new value
        if scatter_canvas:
            scatter_canvas.get_tk_widget().destroy()
            
        if bar_canvas:
            bar_canvas.get_tk_widget().destroy()
            
        if density_canvas:
            density_canvas.get_tk_widget().destroy()
            
        if heatmap_canvas:
            heatmap_canvas.get_tk_widget().destroy()
            
    if selected_column2:
        inner_frame.destroy()
        inner_frame = tk.Frame(canvas, background="#350097")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        inner_frame.bind("<Configure>", lambda evt: canvas.configure(scrollregion=canvas.bbox("all")))
        labels(data[[selected_column1, selected_column2]], inner_frame)
    combobox1.set(selected_column2)

# Creating a tkinter 
app = tk.Tk()
app.title("CSV data analysis")
app.attributes("-fullscreen", True)
app.config(background="#0B0047")

# Create a frame
frame = tk.Frame(app, background="#0068D5", width=1550, height=60)
frame.place(x=0, y=40)

# The data analysis title
Title = tk.Label(frame, text="AnalystCX (CSV files)")
Title.configure(font=("Berlin Sans FB", 35), background="#0068D5", foreground="white")
Title.place(x=700, y=0)

# Canvas for displaying the CSV cells
canvas = tk.Canvas(app, width=350, height=500, background="#350097", highlightthickness=0)
canvas.place(x=0, y=102)

# Vertical scrollbar
scrollbar = tk.Scrollbar(frame, command=canvas.yview)
scrollbar.pack(side="right", fill="y")
scrollbar.place(x=350, y=750, relheight=1)
canvas.configure(yscrollcommand=scrollbar.set)

# Horizontal scrollbar
scrollbar_x = ttk.Scrollbar(app, orient="horizontal", command=canvas.xview)
scrollbar_x.place(x=0, y=605, width=350)
canvas.configure(xscrollcommand=scrollbar_x.set)

inner_frame = tk.Frame(canvas, background="#350097") 
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Creating a scrollbar activation on inner frame
inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Browsing CSV button
button_browse = tk.Button(app, font=("Berlin Sans FB", 15), text="Browse CSV files", width=18, height=2, command=lambda: open_csv(inner_frame), background="#00C300", foreground="White")
button_browse.place(x=0, y=40)

# Frame1
frame1 = tk.Frame(app, background="#270077", width=595, height=380)
frame1.place(x=355, y=102)

# Frame2
frame2 = tk.Frame(app, background="#270077", width=595, height=380)
frame2 .place(x=355, y=489)

# Graph 3
frame3 = tk.Frame(app, background="#270077", width=595, height=380)
frame3 .place(x=955, y=102)

# Graph 4
frame4 = tk.Frame(app, background="#270077", width=595, height=380)
frame4 .place(x=955, y=489)

# Choosing title
Title1 = tk.Label(app, text="Choose X and Y values")
Title1.configure(font=("Berlin Sans FB", 25), background="#0B0047", foreground="#FDCBFF")
Title1.place(x=20, y=640)

# X values
x_value = tk.Label(app, text="Input x values: ")
x_value.configure(font=("Berlin Sans FB", 15), background="#0B0047", foreground="#FDCBFF")
x_value.place(x=10, y=694)

# y value
y_value = tk.Label(app, text="Input y values: ")
y_value.configure(font=("Berlin Sans FB", 15), background="#0B0047", foreground="#FDCBFF")
y_value.place(x=10, y=776)

# X and y value combobox
combobox = ttk.Combobox(app, state="read", font=("Comic Sans MS", 10, "bold"), foreground="black", width=20)
combobox.place(x=140, y=700)
combobox.bind("<<ComboboxSelected>>", drop_combobox)

# Combobox for selecting thd data
combobox1 = ttk.Combobox(app, state="read", font=("Comic Sans MS", 10, "bold"), foreground="black", width=20)
combobox1.place(x=140, y=780)
combobox1.bind("<<ComboboxSelected>>", drop_combobox1)

# graph creating button
bargraph = tk.Button(app, font=("Berlin Sans FB", 13), text="Create Bar graph", width=14, height=1, command=bar, background="#FF7100", foreground="White")
bargraph.place(x=815, y=102)

# Scatter plot display
scatter1 = tk.Button(app, font=("Berlin Sans FB", 13), text="Create Scatter plot", width=16, height=1, command=scatter, background="#FF7100", foreground="White")
scatter1.place(x=1380, y=102)

# Create a button to create the density plot
density_plot_button = tk.Button(app, font=("Berlin Sans FB", 13), text="Create Density Plot", width=16, height=1, command=density_plot, background="#FF7100", foreground="White")
density_plot_button.place(x=795, y=489)

# Area chart displaying
area_charting = tk.Button(app, font=("Berlin Sans FB", 13), text="Create Area Chart", width=16, height=1, command=heatmap, background="#FF7100", foreground="White")
area_charting.place(x=1380, y=489)

# Exit button
buttonexits = tk.Button(app, font=("Berlin Sans FB", 15), text="X", width=10, height=1, command=quit, background="#D30000", foreground="White")
buttonexits.place(x=1427, y=0)

app.mainloop()
