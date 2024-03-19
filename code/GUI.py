import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from execute_program import Execute
from process_program import Process

class SimpleGUI:
    '''This class creates a simple GUI using tkinter'''
    def __init__(self, sim, memory):
        self.main = tk.Tk()  # create the main gui window
        self.main.title("UVSIM")  # title of main window
        self.main.geometry("500x500") # dimensions of main window
        self.main.configure(bg="lightblue")  # main window color
        self.sim = sim
        self.memory = memory

        # create menu bar
        self.menu_bar = tk.Menu(self.main)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  # create file menu
        self.file_menu.add_command(label="Open", command=self.open_file)  # call open_file
        self.file_menu.add_command(label="Save Code Block", command=self.save_code_block)  # call save_code_block
        self.file_menu.add_command(label="Run Code Block", command=self.run_code_block)  # call run_code_block
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)  # add file menu to menu bar
        self.main.config(menu=self.menu_bar)  # add menu bar to main window  # put text widget in block
        
        # label for main window with initial file select message
        self.label_1 = tk.Label(self.main, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label_1.pack(pady=10)

        # labels for code block and code text
        self.label_2 = tk.Label(self.main, text="UVSim code block")
        self.code_text = tk.Text(self.main, height=10, width=40)
        self.label_2.pack(pady=10)
        self.code_text.pack(pady=10)

        # output sim operation log to user
        self.label_3 = tk.Label(self.main, text="UVSim operations log")
        self.operations_text = tk.Text(self.main, height=10, width=40, state=tk.DISABLED)  #Read-only
        self.label_3.pack(pady=10)
        self.operations_text.pack(pady=10)

        self._program = []  # initialize empty program

    def open_file(self):
        # search directories and choose a txt file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.code_text.delete(1.0, tk.END)  # clear previous input
        if file_path:
            try:                         
                program = Process.read_txt(file_path)
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
                with open(file_path, 'w') as file:
                    file.write(self.code_text.get(1.0, tk.END))
                    self._program = [int(line.strip()) for line in self.code_text.get(1.0, tk.END).split("\n") if line.strip()]
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_code_block(self):
        program = [int(line.strip()) for line in self.code_text.get(1.0, tk.END).split("\n") if line.strip()]
        try:
            self.memory.load_program(program)   # load program from the user text input into the sim
            Execute.execute_program(self.sim, self, self.memory)  # execute program with Execute class
            self.final_output()  # output accumulator value in gui
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def final_output(self):
        # output accumulator value to gui
        output = f"Final accumulator value: {self.sim._accumulator}\n"
        self.operations_text.config(state=tk.NORMAL)
        self.operations_text.insert(tk.END, output)
        self.operations_text.config(state=tk.DISABLED)
        messagebox.showinfo("Result: ", f"Final Accumulator Value: {self.sim._accumulator}") 

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
        output = f"Write Op: Value at register {self.sim._operand}: {value}\n"
        self.operations_text.config(state=tk.NORMAL)
        self.operations_text.insert(tk.END, output)
        self.operations_text.config(state=tk.DISABLED)

    def too_long(self):
        # gui error message if sim pc exceeds available memory
        messagebox.showerror("Error", "Program too long.")
