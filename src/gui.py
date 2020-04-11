from tkinter import *
from bubble_sort import *
from quick_sort import *
from merge_sort import *
from insertion_sort import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Alogorith Visualisation')
root.maxsize(900,600)
root.config(bg= 'black')# customize color of the bg later
data = []

#variables 
seleceted_alg = StringVar()

def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [n / max(data) for n in data]
    for i, height in enumerate(normalized_data):
        #top left 
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right 
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0,y0, x1, y1, fill = color_array[i])
        canvas.create_text(x0+2,y0,anchor =SW, text = str(data[i]))
    root.update_idletasks()

def Generate():
    global data

    min_Val = int(min_entry.get())
    max_Val = int(max_entry.get())
    size = int(size_entry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(min_Val, max_Val + 1))
    draw_data(data, ["red" for x in range(len(data))]) # ['red','red'...]


def start_algorithm():
    global data
    if not data: return 

    if(alg_menu.get() == 'Quick sort'):
        quick_sort(data, 0,len(data) - 1,draw_data,speed_scale.get())
    elif alg_menu.get() == 'Bubble sort':
        bubble_sort(data,draw_data,speed_scale.get())
    elif alg_menu.get() == 'Merge sort':
        merge_sort(data, draw_data, speed_scale.get())
    elif alg_menu.get() == 'Insertion sort':
        insertion_sort(data, draw_data, speed_scale.get())
    draw_data(data,[['green'] for x in range(len(data))])

#frame / base layout
UI_frame = Frame(root,width = 600,height= 200, bg = 'white')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root,width=600, height = 380, bg = 'white')
canvas.grid(row = 1,column = 0,padx = 10, pady =5)

#User Interface Area
#row --> 0 
Label(UI_frame, text="Algorithm: ", bg = 'white',fg = 'black',font = ('Calibri',30)).grid(row = 0, column = 0,padx= 5, pady= 5, sticky = W)
alg_menu = ttk.Combobox(UI_frame,textvariable=seleceted_alg, values=['Bubble sort','Merge sort','Quick sort','Insertion sort'])
alg_menu.grid(row = 0, column = 1,padx = 5, pady = 5)
alg_menu.current(0)


speed_scale = Scale(UI_frame, from_= 0.1, to= 2.0, length = 200, digits=2, resolution= 0.2, orient=HORIZONTAL, label="select speed [s]")
speed_scale.grid(row = 0, column = 2, padx = 5, pady = 5)
Button(UI_frame, text = 'start', command= start_algorithm, bg ='green').grid(row = 0,column=3,padx=5,pady=5)

#row --> 1 

# size

size_entry = Scale(UI_frame, from_= 3, to= 25, length = 200,resolution= 1, orient=HORIZONTAL, label="Data Size ")
size_entry.grid(row = 1,column = 0, padx = 5)

# min_val
min_entry = Scale(UI_frame, from_= 1, to= 10, length = 200, resolution= 1, orient=HORIZONTAL, label="Minimum")
min_entry.grid(row = 1,column = 1, padx = 5)

# max_val
max_entry = Scale(UI_frame, from_= 10, to= 100, length = 200, resolution= 1, orient=HORIZONTAL, label="Maximum")
max_entry.grid(row = 1,column = 2, padx = 5)

Button(UI_frame, text = 'Generate', command= Generate, bg ='red').grid(row = 1,column=3,padx=5,pady=5)
#row --> 2  

root.mainloop()