from math_functions import *
import tkinter

display_content = ""
max_display_length = 21

def mouse_click(event):
    x = (event.x - 5*2) // 100
    y = (event.y - 2*10 - 90) // 100
    index = x + 4*y
    display_add_by_click(buttons[index][1])

def display_add_by_click(char):
    global display_content
    if len(char) == 1:
        if 48 <= ord(char) and ord(char) <= 57 and len(display_content) <= max_display_length:
            display_content += char
            canvas.delete("displayed")
            canvas.create_text(390, 55,text = display_content,font="Times 25", anchor="e", tag = "displayed")

def display_add(event):
    global display_content
    if 48 <= ord(event.char) and ord(event.char) <= 57 and len(display_content) <= max_display_length:
        display_content += event.char
        canvas.delete("displayed")
        canvas.create_text(390, 55,text = display_content,font="Times 25", anchor="e", tag = "displayed")

def binds():
    canvas.bind('<Button-1>', mouse_click)

    canvas.bind_all("<Key>", display_add)

def gui_ctor():
    global canvas, buttons
    WIDTH = 410
    HEIGHT = 615
    canvas = tkinter.Canvas(width = WIDTH, height = HEIGHT, background='lightblue')
    canvas.pack()

    binds()

    display = (5,10,405,100)
    canvas.create_rectangle(display, width = 2, fill = "white")
    button_height = 100
    button_width = 100
    buttons = (
        ((5,110,105,210), "xⁿ ", "lightgrey", exponentiate),
        ((105,110,205,210), "ⁿ√x", "lightgrey"),
        ((205,110,305,210), "|x|", "lightgrey"),
        ((305,110,405,210), "C", "snow4"),

        ((5,210,105,310), "7", "white"),
        ((105,210,205,310), "8", "white"),
        ((205,210,305,310), "9", "white"),
        ((305,210,405,310), "!", "lightgrey"),

        ((5,310,105,410), "4", "white"),
        ((105,310,205,410), "5", "white"),
        ((205,310,305,410), "6", "white"),
        ((305,310,405,410), "÷", "lightgrey"),

        ((5,410,105,510), "1", "white"),
        ((105,410,205,510), "2", "white"),
        ((205,410,305,510), "3", "white"),
        ((305,410,405,510), "*", "lightgrey"),

        ((5,510,105,610), "0", "white"),
        ((105,510,205,610), "-", "lightgrey"),
        ((205,510,305,610), "+", "lightgrey"),
        ((305,510,405,610), "=", "tomato")
    )

    for button in buttons:
        coordinations = button[0]
        canvas.create_rectangle(coordinations, fill = button[2], width = 2, outline = 'black')
        text_x = coordinations[0]+button_width//2
        text_y = coordinations[1]+button_height//2
        button_text = button[1]
        canvas.create_text(text_x, text_y, text = button_text, font="Times 20 bold")

gui_ctor()

canvas.mainloop()