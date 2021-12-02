#! /usr/bin/env python

import tkinter as tk
from tkinter import ttk

FORMULA_FONT_STYLE = ("Arial", 16)
TOTAL_FONT_STYLE = ("Arial", 32)
BUTTON_FONT = ("Operator Mono Lig", 24, "italic")
BUTTON_FONT_COLOR = "#fcfcfc"
BUTTON_COLOR = "#162330"
BUTTON_OPERATOR_COLOR = "#283442"
LABEL_TEXT_COLOR = "#fcfcfc"
DISPLAY_LABEL_COLOR = "#193049"

class Calculator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x900")
        self.window.resizable(0, 0)

        self.total = "0"
        self.formula = ""
        # Use a dictionary to display numbers. [column, row, columnspan]
        self.button_dict = {7: [0, 1, 1], 8: [1, 1, 1], 9:[2, 1, 1],
                            4: [0, 2, 1], 5: [1, 2, 1], 6:[2, 2, 1],
                            1: [0, 3, 1], 2: [1, 3, 1], 3:[2, 3, 1], 0: [0, 4, 2], ".": [2, 4, 1], 
                            }

        self.operators = {"/": [3, 0], "*": [3, 1], "-": [3, 2], "+": [3, 3], "%": [2, 0]}

        self.display_frame = self.create_display_frame()
        self.display_formula, self.display_total = self.create_display_label()

        self.button_frame = self.create_button_frame()
        

        # Calls button creation methods
        self.create_buttons()
        self.create_operations_buttons()
        self.create_clear_button()
        self.create_equals_button()
        for i in range(0, 5):
            self.button_frame.rowconfigure(i, weight=1)
        for i in range(0, 4):
            self.button_frame.columnconfigure(i, weight=1)



    def create_display_label(self):
        formula_label = tk.Label(self.display_frame, text=self.formula,
                               bg=DISPLAY_LABEL_COLOR,fg=LABEL_TEXT_COLOR, font=FORMULA_FONT_STYLE, 
                               anchor=tk.E)
        formula_label.pack(expand=True, fill="both")

        total_label = tk.Label(self.display_frame, text=self.total,
                               bg=DISPLAY_LABEL_COLOR,fg=LABEL_TEXT_COLOR, font=TOTAL_FONT_STYLE, 
                               anchor=tk.E)
        total_label.pack(expand=True, fill="both")
       
        return formula_label, total_label
    

    def create_buttons(self):
        for number, grid_value in self.button_dict.items():
            button = tk.Button(self.button_frame, text=str(number), font=BUTTON_FONT, 
                               bg=BUTTON_COLOR, fg=BUTTON_FONT_COLOR, command=lambda x = number: self.enter_value(str(x)))
            button.grid(column=grid_value[0], row=grid_value[1], columnspan=grid_value[2], sticky=tk.NSEW)

        
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="c", font=BUTTON_FONT, 
                           bg=BUTTON_OPERATOR_COLOR, fg=BUTTON_FONT_COLOR, command=lambda: self.clear_value())
        button.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW)


    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", font=BUTTON_FONT,
                           bg=BUTTON_OPERATOR_COLOR, fg=BUTTON_FONT_COLOR, command=lambda: self.evaluate_formula())
        button.grid(column=3, row=4, sticky=tk.NSEW)


    def create_operations_buttons(self):
        for symbol, grid_value in self.operators.items():
            button = tk.Button(self.button_frame, text=str(symbol), font=BUTTON_FONT, 
                               bg=BUTTON_OPERATOR_COLOR, fg=BUTTON_FONT_COLOR, command=lambda x = symbol: self.operations(x))
            button.grid(column=grid_value[0], row=grid_value[1], sticky=tk.NSEW)

 
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=200)
        frame.pack(expand=True, fill="both")
        return frame

    def enter_value(self, value):
        if self.total == "0":
            self.total = value
            self.formula += self.total
            self.update_total()
            self.update_formula()
        else:
            self.total += value
            self.formula += value
            self.update_total()
            self.update_formula()
   
    
    def operations(self, operator):
        if operator in self.formula:
            self.formula = self.formula
        else:
            self.formula += operator
            self.update_formula()
            self.total = ""
            self.update_total()


    def evaluate_formula(self):
        self.total = eval(self.formula)
        self.update_total()
        self.formula = str(self.total)
        self.update_formula()


    def clear_value(self):
        self.total = "0"
        self.update_total()
        self.formula = ""
        self.update_formula()


    def update_total(self):
        self.display_total.config(text=self.total)        


    def update_formula(self):
        self.display_formula.config(text=self.formula)


    def create_button_frame(self):
        frame = tk.Frame(self.window, height=700)
        frame.pack(expand=True, fill="both")
        return frame
   

    def run(self):
        self.window.mainloop()


calc = Calculator()
calc.run()
    
        
