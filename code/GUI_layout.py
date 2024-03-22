import tkinter as tk
from tkinter import messagebox

class GUILayout:
    '''This class creates the GUI using tkinter'''
    def __init__(self):
        self.main = tk.Tk()  # create the main gui window
        self.main.title("UVSIM")  # title of main window
        self.main.configure(bg="#4C721D")  # main window color
        self.main.geometry("500x500") # dimensions of main window

        # create menu bar
        self.menu_bar = tk.Menu(self.main)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  # create file menu
        self.file_menu.add_command(label="Open", command=self.open_file)  # call open_file
        self.file_menu.add_command(label="Save Code Block", command=self.save_code_block)  # call save_code_block
        self.file_menu.add_command(label="Run Code Block", command=self.run_code_block)  # call run_code_block
        self.file_menu.add_command(label="Configure Color Scheme", command=self.configure_color_scheme)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)  # add file menu to menu bar
        self.main.config(menu=self.menu_bar)  # add menu bar to main window 
        
        # create labels and text box widgets
        self.label_1 = tk.Label(self.main, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label_2 = tk.Label(self.main, text="UVSim code block")
        self.label_3 = tk.Label(self.main, text="UVSim operations log")
        self.code_text = tk.Text(self.main, height=10, width=40)
        self.operations_text = tk.Text(self.main, height=10, width=40, state=tk.DISABLED)  #Read-only
        self.code_text.bind("<Key>", self.limit_code_lines)  # limit the number of lines in the code block
        
        # pack widgets and set default off color
        widgets = [self.label_1, self.label_2, self.code_text, self.label_3, self.operations_text]
        for widget in widgets:
            widget.pack(pady=10)
            widget.configure(bg="#FFFFFF", fg="#000000")
    
    def limit_code_lines(self, event):
    # limit the number of lines in the code block
        current_text = self.code_text.get("1.0", "end-1c")  # Get the current text in the code block
        non_empty_lines = [line for line in current_text.split("\n") if line.strip()]  # Filter out empty lines
        current_lines = len(non_empty_lines)  # Count the non-empty lines
        # if the number of lines exceeds 100, delete the last line
        if current_lines > 100:
            # delete the last line
            self.code_text.delete(f"{current_lines}.0", tk.END)
            messagebox.showwarning("Warning", "Only 100 registers are available. Please remove some lines and try again")
