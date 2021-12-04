#! /usr/bin/env python
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile
import sys
import os

FONT = ("Operator Mono Lig", 12, "italic")
TEXTBOX_COLOR = "#343642"
TEXTBOX_FONT_COLOR = "#ffffff"


class Main:

    def __init__(self):
        self.file_list = []
        self.file = ""
        self.file_number = 0
        self.path = "/home/jas/Documents/reference/"

        # Declare the main window
        self.window = tk.Tk()
        # Set window geometry
        self.window.geometry("1600x1900")
        # Disable window resizing
        self.window.resizable(0, 0)

        # Create a frame within the window
        self.textbox_frame = tk.Frame(self.window, padx=10, pady=10, bg=TEXTBOX_COLOR)
        self.textbox_frame.pack(expand=1, fill="both")

        # Create the text box
        self.textbox = tk.Text(self.textbox_frame, bg=TEXTBOX_COLOR, font=FONT, 
                               fg=TEXTBOX_FONT_COLOR, relief="ridge", wrap="word", bd=9,
                               insertbackground="#ffffff")
        self.textbox.pack(expand=1, fill="both")
        
        
        # Start the notepad with file0
        self.note_start()

        # Create a label to display file name
        self.file_label = tk.Label(self.textbox_frame, text=self.file_list[self.file_number], bg=TEXTBOX_COLOR, fg=TEXTBOX_FONT_COLOR)
        self.file_label.pack(anchor="w")


        # Keybinds
        self.textbox.bind("<Control_L>s", self.save_as_file)
        self.textbox.bind("<Control_L>l", self.load_file)
        self.textbox.bind("<F1>", self.cycle_files_down)
        self.textbox.bind("<F2>",  self.cycle_files_up)
        self.textbox.bind("<Control_L>n", self.newfile)
       

    def save_as_file(self, event):
        self.get_files()
        if self.file in self.file_list:
            with open(self.path + self.file_list[self.file_number], "w+") as self.file:
                text = self.textbox.get(1.0, "end")
                self.file.write(text)
        else:
            text = self.textbox.get(1.0, "end")
            self.file = asksaveasfile(defaultextension=".txt")
            self.file.write(text)


    def newfile(self, event):
        self.textbox.delete(1.0, "end")
        self.file = asksaveasfile(initialdir=self.path, defaultextension=".txt")
        if self.file:
            text = self.textbox.get(1.0, "end")
            self.file.write(text)
            self.get_files()
            for file, index in enumerate(self.file_list):
                if self.file == file:
                    self.file_number = index
            self.file_label.config(text=self.file_list[self.file_number])


    def load_file(self, event):
        self.file = askopenfile(parent=self.window, mode="rb", title="Choose a file")
        if self.file:
            self.textbox.insert(1.0, self.file.read())


    def get_files(self):
        files = os.listdir(self.path)
        for f in files:
            if f not in self.file_list and ".txt" in f:
                self.file_list.append(f)


    def note_start(self):
        self.get_files()
        with open(self.path + self.file_list[self.file_number]) as file:
            text = file.read()
            self.textbox.insert(1.0, text)
        self.file = self.file_list[self.file_number]
        self.textbox.focus_set()
        

    def cycle_files_up(self, event):
        self.get_files()
        textbox_text = self.textbox.get(1.0, "end")

        with open(self.path + self.file_list[self.file_number], "w+") as file:
            file_text = file.read()
            if len(textbox_text) != len(file_text):
                file.write(textbox_text)

        if self.file_number == len(self.file_list) - 1:
            self.file_number = 0
        else:
            self.file_number += 1

        with open(self.path + self.file_list[self.file_number]) as file:
            file_text = file.read()
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0, file_text)
            self.file_label.config(text=self.file_list[self.file_number])
            self.file = self.file_list[self.file_number]


    def cycle_files_down(self, event):
        self.get_files()
        textbox_text = self.textbox.get(1.0, "end")

        with open(self.path + self.file_list[self.file_number], "w+") as file:
            file_text = file.read()
            if len(textbox_text) != len(file_text):
                file.write(textbox_text)

        if self.file_number == 0:
            self.file_number = len(self.file_list) - 1
        else:
            self.file_number -= 1

        with open(self.path + self.file_list[self.file_number]) as file:
            file_text = file.read()

        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, file_text)
        self.file_label.config(text=self.file_list[self.file_number])
        self.file = self.file_list[self.file_number]


    def run(self):
        self.window.mainloop()


app = Main()
app.run()
