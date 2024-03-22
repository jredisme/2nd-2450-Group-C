import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from execute_program import Execute
from process_program import Process
import os

class SimpleGUI:
    '''This class creates a simple GUI using tkinter'''
    def __init__(self, sim, memory):
        self.main = tk.Tk()  # create the main gui window
        self.main.title("UVSIM")  # title of main window
        self.main.configure(bg="#4C721D")  # main window color
        self.main.geometry("500x500") # dimensions of main window
        self.sim = sim
        self.memory = memory
        self._program = []  # initialize empty program

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

    def open_file(self):
        # search directories and choose a txt file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.code_text.delete(1.0, tk.END)  # clear previous input
        if file_path:
            try:                         
                program = Process.read_txt(file_path)
                # only take the first 100 lines of the file
                if len(program) > 100:
                    program = program[:100] # take the first 100 lines
                    messagebox.showwarning("Warning", "Only 100 registers are available. Only the first 100 lines will be used. Please remove some lines and try again")
                for line in program:
                    self.code_text.insert(tk.END, f"{line}\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No file selected.")   

    def save_code_block(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:  # Open file in write mode ('w')
                    lines = self.code_text.get(1.0, tk.END).split("\n")
                    stripped_lines = [line.strip() for line in lines if line.strip()]  # Strip leading and trailing whitespace
                    file.write("\n".join(stripped_lines))
                    self._program = [int(line.strip()) for line in stripped_lines]
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_code_block(self):
        program = [int(line.strip()) for line in self.code_text.get(1.0, tk.END).split("\n") if line.strip()]
        try:
            self.memory.load_program(program)   # load program from the user text input into the sim
            Execute.execute_program(self.sim, self, self.memory)  # execute program with Execute class
            self.output(f"Final accumulator value: {self.sim._accumulator}\n\n")  # output accumulator value in gui
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def configure_color_scheme(self):
        # Function to configure color scheme
        primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
        off_color = colorchooser.askcolor(title="Choose Off Color")[1]
        # Apply the chosen colors to the GUI
        self.main.configure(bg=primary_color)
        widgets_off_color = [self.label_1, self.label_2, self.label_3, self.code_text, self.operations_text]
        for widget in widgets_off_color:
            widget.configure(bg=off_color)

    def output(self, output):
        # output to gui
        self.operations_text.config(state=tk.NORMAL)
        self.operations_text.insert(tk.END, output)
        self.operations_text.config(state=tk.DISABLED)

    def read(self):
        #Read a word from the keyboard into memory
        entry_window = tk.Toplevel(self.main)  # create user input window
        entry_window.title("Enter Value")
        entry_window.geometry("300x100")

        def submit():
            try:
                value = int(entry.get())  #check for int
                value = self.memory.truncate(value)  #truncate if the user value exceeds 4 digits
                self.memory._registers[self.sim._operand] = value  # place user input into memory
                entry_window.destroy()  # close user input window
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        # label and button for user input
        entry_label = tk.Label(entry_window, text=f"Enter a number for memory location {self.sim._operand}:")
        entry_label.pack(pady=5)
        entry = tk.Entry(entry_window)
        entry.pack(pady=5)
        submit_button = tk.Button(entry_window, text="Submit", command=submit)
        submit_button.pack(pady=5)
        
        entry_window.wait_window()  #wait for user input before continuing
    
    def write(self):
        # write a word from memory to gui
        value = self.memory._registers[self.sim._operand]
        self.output(f"Write Op: Value at register {self.sim._operand}: {value}\n")
