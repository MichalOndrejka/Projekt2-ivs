from math_functions import *
import tkinter

default_display_value = "0.0"
display_content = default_display_value
max_display_length = 21
operation  = None
operand1 = None
operand2 = default_display_value

def find_value_in_nested_array(value, array):
    for index, nested_array in enumerate(array):
        if value in nested_array:
            return index
    return None

def is_number(symbol):
    if len(symbol) == 1:
        if 48 <= ord(symbol) and ord(symbol) <= 57:
            return True
    return False

def display_add(clear, value):
    global display_content
    if clear == True or display_content == default_display_value:
        display_content = ""
    display_content += value
    canvas.delete("displayed")
    canvas.create_text(390, 55,text = display_content,font="Times 25", anchor="e", tag = "displayed")

def handle_symbol(symbol):
    global display_content, operand1, operand2, operation

    if is_number(symbol) and len(display_content) <= max_display_length:
        display_add(False, symbol)
        operand2 = display_content
    else:
        index = find_value_in_nested_array(symbol, buttons)
        if index != None:
            if buttons[index][3] == equals:
                equals()
            elif buttons[index][3] == clear_operands:
                clear_operands()
            else:
                operation = buttons[index][3]
                operand1 = operand2
                operand2 = None
                display_content = default_display_value

def mouse_clicked(event):
    x = (event.x - 5*2) // 100
    y = (event.y - 2*10 - 90) // 100
    index = x + 4 * y
    if 0 <= index and index <= 19:
        handle_symbol(buttons[index][1])

def key_pressed(event):
    if event.keysym == "Enter":
        handle_symbol("=")
    else:
        handle_symbol(event.char)

def binds():
    canvas.bind('<Button-1>', mouse_clicked)
    canvas.bind_all("<Key>", key_pressed)

def gui_ctor():
    global canvas, buttons

    canvas_width = 410
    canvas_height = 615
    canvas = tkinter.Canvas(width = canvas_width, height = canvas_height, background='lightblue')
    canvas.pack()

    binds()

    outline_width = 2
    display = (5,10,405,100)
    canvas.create_rectangle(display, width = outline_width, fill = "white")
    buttons = (
        ((5,110,105,210), "xⁿ ", "lightgrey", exponentiate),
        ((105,110,205,210), "ⁿ√x", "lightgrey", nthroot),
        ((205,110,305,210), "|x|", "lightgrey", absolute),
        ((305,110,405,210), "C", "snow4", clear_operands),

        ((5,210,105,310), "7", "white", None),
        ((105,210,205,310), "8", "white", None),
        ((205,210,305,310), "9", "white", None),
        ((305,210,405,310), "!", "lightgrey", factorial),

        ((5,310,105,410), "4", "white", None),
        ((105,310,205,410), "5", "white", None),
        ((205,310,305,410), "6", "white", None),
        ((305,310,405,410), "÷", "lightgrey", divide),

        ((5,410,105,510), "1", "white", None),
        ((105,410,205,510), "2", "white", None),
        ((205,410,305,510), "3", "white", None),
        ((305,410,405,510), "*", "lightgrey", multiply),

        ((5,510,105,610), "0", "white", None),
        ((105,510,205,610), "-", "lightgrey", subtract),
        ((205,510,305,610), "+", "lightgrey", addition),
        ((305,510,405,610), "=", "tomato", equals)
    )

    for button in buttons:
        coordinations = button[0]
        button_color = button[2]
        canvas.create_rectangle(coordinations, fill = button_color, width = outline_width, outline = 'black')
        text_x = (coordinations[0]+coordinations[2])//2
        text_y = (coordinations[1]+coordinations[3])//2
        button_text = button[1]
        canvas.create_text(text_x, text_y, text = button_text, font="Times 20 bold")
    
    display_add(True, default_display_value)

def calculate(operation, operand1, operand2):
    if operand1 != None:
        operand1 = float(operand1)
    if operand2 != None:
        operand2 = float(operand2)
    result = None
    if operation != absolute and operation != factorial:
        if operand1 != None and operand2 != None:
            result = operation(operand1, operand2)
    else:
        if operand1 != None:
            result = operation(int(operand1))
    return result

def equals():
    global operand1, operand2, operation
    result = str(calculate(operation, operand1, operand2))
    if result != None:
        display_add(True, result)
    operand2 = result
    operand1 = None

def clear_operands():
    global operand1, operand2, operation
    operand1 = None
    operand2 = None
    operation = None
    display_add(True, default_display_value)

gui_ctor()

canvas.mainloop()