import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from execute_program import Execute


class SimpleGUI:
    '''This class creates a simple GUI using tkinter'''
    def __init__(self, sim):
        self.main = tk.Tk()  # create the main gui window
        self.main.title("UVSIM")  # title of main window
        self.main.geometry("500x500") # dimensions of main window
        self.main.configure(bg="lightblue")  # main window color
        self.sim = sim

        # label for main window with initial file select message
        self.label = tk.Label(self.main, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label.pack(pady=10)

        # file select submit button
        self.file_button = tk.Button(self.main, text="Select File", command=self.select_file) # call select_file
        self.file_button.pack()  # put button in block

        self.exit_button = tk.Button(self.main, text="Exit", command=self.destroy_program) # call main.destroy
        self.exit_button.pack(side=tk.BOTTOM, pady=10)
        self.exit_button.config(height=2, width=10)

        # output sim operation log to user
        self.label = tk.Label(self.main, text="UVSim operations log")
        self.operations_text = tk.Text(self.main, height=10, width=40)
        self.operations_text.pack(pady=10)

        self._program = []  # initialize empty program

    def select_file(self):
        # search directories and choose a txt file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        self._program.append(int(line.strip()))  # add each line of program to program, check for int
                self.load_file()   # load program into sim
                Execute.execute_program(self.sim, self)  # execute program with Execute class
                self.final_output()  # output accumulator value in gui  # ask user for next action
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No file selected.")

    def destroy_program(self):
        sys.exit()

    def load_file(self):
        # load program from the user-selected file into the sim
        self.sim.load_ml_program(self._program)

    def operations_output(self, op, func_name, operand):
        if op == 11:
            output = f"Memory Location {operand}: {self.sim._memory[operand]}\n"
            self.operations_text.insert(tk.END, output)


    def final_output(self):
        # output accumulator value in gui
        output = f"Final accumulator value: {self.sim._accumulator}\n"
        self.operations_text.insert(tk.END, output)
        # messagebox.showinfo("Result: ", f"Final Accumulator Value: {self.sim._accumulator}")

    def read(self):
        #Read a word from the keyboard into memory
        entry_window = tk.Toplevel(self.main)  # create user input window
        entry_window.title("Enter Value")
        entry_window.geometry("300x100")

        def submit():
            try:
                value = int(entry.get())  #check for int
                self.sim._memory[self.sim._operand] = value  # place user input into memory
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
        self.sim._memory[self.sim._operand]
        # self.operations_text.insert(tk.END, f"Memory Location {self.sim._operand}: {self.sim._memory[self.sim._operand]}\n")
    #     # messagebox.showinfo("Write Operation", f"Value at memory location {self.sim._operand}: {value}")

    def too_long(self):
        # gui error message if sim pc exceeds available memory
        messagebox.showerror("Error", "Program too long.")
