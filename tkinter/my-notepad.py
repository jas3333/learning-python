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
        self.window.geometry("1000x1300")
        self.window.title("My-Notepad")
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
        self.textbox.bind("<F1>", self.cycle_files_down)
        self.textbox.bind("<F2>",  self.cycle_files_up)
        self.textbox.bind("<Control_L>n", self.ask_file_name)
       

    # Will save the file if ctrl + s is hit. 
    def save_as_file(self, event):
        self.get_files()
        if self.file in self.file_list:
            with open(self.path + self.file_list[self.file_number], "w+") as self.file:
                text = self.textbox.get(1.0, "end")
                self.file.write(text)
        # I don't think this is needed with this type of notepad since the file will
        # always be in the file_list
        else:
            text = self.textbox.get(1.0, "end")
            self.file = asksaveasfile(defaultextension=".txt")
            self.file.write(text)


    # Creates a popup window with an entry widget so we can get the
    # user to enter a new file name
    def ask_file_name(self, event):
        create_new_window = tk.Toplevel(self.window)
        create_new_window.geometry("300x100")
        create_new_window.resizable(0, 0)
        create_new_window.focus_set()
        
        entry_box = tk.Entry(create_new_window)
        entry_box.pack()

        # This button will pass the file name and window to get_file_name
        # so it can get info and close the window
        ok_button = tk.Button(create_new_window, text="Ok", command=lambda:self.get_file_name(entry_box, create_new_window))
        ok_button.pack()

        cancel_button = tk.Button(create_new_window, text="Cancel", command=lambda: create_new_window.destroy())
                

    
    # Gets the new file name from ask_file_name and creates a new file 
    def get_file_name(self, filename, popup):
        self.textbox.delete(1.0, "end")
        text = self.textbox.get(1.0)
        self.file = filename.get()  
        file = self.file
        # Kills the popup window after getting the info from it
        popup.destroy()

        with open(self.path + file, "w+") as file:
            file.write(text)
        self.get_files()
        
        # Updates the file_lable file so we can see what file we currently are using
        for index, file in enumerate(self.file_list):
            print(f"Index: {index} File: {file} Filename: {self.file}")
            if self.file == file:
                self.file_number = index
        # Updates the file_label
        self.file_label.config(text=self.file_list[self.file_number])


    # Get files in a directory and append them to a list
    def get_files(self):
        files = os.listdir(self.path)
        for f in files:
            if f not in self.file_list and ".txt" in f:
                self.file_list.append(f)


    # Start the notebook using file in file_list[0]
    def note_start(self):
        self.get_files()
        with open(self.path + self.file_list[self.file_number]) as file:
            text = file.read()
            self.textbox.insert(1.0, text)
        self.file = self.file_list[self.file_number]
        self.textbox.focus_set()
        

    # Cycle up through the txt files in reference directory
    def cycle_files_up(self, event):
        # Update the file list 
        self.get_files()
        textbox_text = self.textbox.get(1.0, "end")

        # This will check if there are any changes in the current file.
        # If there is it will save the file before loading up the next.
        with open(self.path + self.file_list[self.file_number], "w+") as file:
            file_text = file.read()
            if len(textbox_text) != len(file_text):
                file.write(textbox_text)

        # This will make sure we don't get an index out of range error.
        if self.file_number == len(self.file_list) - 1:
            self.file_number = 0
        else:
            self.file_number += 1

        # Gets text from file so we can insert it into textbox 
        with open(self.path + self.file_list[self.file_number]) as file:
            file_text = file.read()

        # Clears the textbox and inserts new text from the new file
        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, file_text)
        self.file_label.config(text=self.file_list[self.file_number])
        self.file = self.file_list[self.file_number]


    # Cycle down through the txt files in reference directory
    def cycle_files_down(self, event):
        self.get_files()
        textbox_text = self.textbox.get(1.0, "end")

        # Checks for any changes in the file and saves if a change was made 
        with open(self.path + self.file_list[self.file_number], "w+") as file:
            file_text = file.read()
            if len(textbox_text) != len(file_text):
                file.write(textbox_text)

        # Sets the list index back kto the top
        if self.file_number == 0:
            self.file_number = len(self.file_list) - 1
        else:
            self.file_number -= 1

        # Open the file and store the text in file_text
        with open(self.path + self.file_list[self.file_number]) as file:
            file_text = file.read()

        # Clear the textbox and insert the text from the new file
        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, file_text)
        self.file_label.config(text=self.file_list[self.file_number])
        self.file = self.file_list[self.file_number]


    def run(self):
        self.window.mainloop()


app = Main()
app.run()
