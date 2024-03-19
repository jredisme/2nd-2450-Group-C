import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from execute_program import Execute
from process_program import Process

class SimpleGUI:
    '''This class creates a simple GUI using tkinter'''
    def __init__(self, sim, memory):
        self.main = tk.Tk()  # create the main gui window
        self.main.title("UVSIM")  # title of main window
        self.main.geometry("500x500") # dimensions of main window
        self.main.configure(bg="#4C721D")  # main window color
        
        self.sim = sim

        self.menu_bar = tk.Menu(self.main)  # create menu bar


        self.memory = memory
        
        # label for main window with initial file select message
        self.label = tk.Label(self.main, text="Welcome to the UVUSIM! Please select a text file to run:")
        self.label.pack(pady=10)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  # create file menu
        self.file_menu.add_command(label="Open", command=self.select_file)  # call select_file
        self.file_menu.add_command(label="Save", command=self.save_file)  # call save_file
        self.file_menu.add_command(label="Run", command=self.load_file)  # call load_file
        self.file_menu.add_command(label="Configure Color Scheme", command=self.configure_color_scheme)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)  # add file menu to menu bar
        self.main.config(menu=self.menu_bar)  # add menu bar to main window  # put text widget in block
        # # file select submit button
        # self.file_button = tk.Button(self.main, text="Select File", command=self.select_file) # call select_file
        # self.file_button.pack()  # put button in block
        # self.save_button = tk.Button(self.main, text="Save", command=self.save_file) # call save_file
        # self.file_button.pack()  # put button in block
        # self.run_button = tk.Button(self.main, text="Run", command=self.load_file) # call load_file
        # self.file_button.pack()  # put button in block

        self.exit_button = tk.Button(self.main, text="Exit", command=self.destroy_program) # call main.destroy
        self.exit_button.pack(side=tk.BOTTOM, pady=10)
        self.exit_button.config(height=2, width=10)

        self.label_2 = tk.Label(self.main, text="UVSim code block")
        self.code_text = tk.Text(self.main, height=10, width=40)
        self.code_text.pack(pady=10)
        # output sim operation log to user
        self.label = tk.Label(self.main, text="UVSim operations log")
        self.operations_text = tk.Text(self.main, height=10, width=40)
        self.operations_text.pack(pady=10)

        self.operations_text.configure(bg="#FFFFFF") #texbox color
        self.code_text.configure(bg="#FFFFFF") #textbox color

        self._program = []  # initialize empty program
        
    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.code_text.get(1.0, tk.END))
                    self._program = [int(line.strip()) for line in self.code_text.get(1.0, tk.END).split("\n") if line.strip()]
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_file(self):
        # search directories and choose a txt file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
                with open(file_path, 'r') as file:
                    for line in file:
                        self._program.append(int(line.strip()))  # add each line of program to program, check for int
                        self.code_text.insert(tk.END, f"{line}")  # output program to gui
            
        else:
            messagebox.showinfo("Info", "No file selected.")
    
    def load_file(self):
        self._program = [int(line.strip()) for line in self.code_text.get(1.0, tk.END).split("\n") if line.strip()]
                # load program from the user-selected file into the sim

        self.sim.load_ml_program(self._program)  # load program into sim
        Execute.execute_program(self.sim, self)  # execute program with Execute class
        self.final_output()  # output accumulator value in gui

        '''try:                         
            program = Process.read_txt(file_path)  # read program with Process class
            self.memory.load_program(program)  # load program into memory
            Execute.execute_program(self.sim, self, self.memory)  # execute program with Execute class
            self.final_output()  # output accumulator value in gui
            self.main.destroy()  # exit gui
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Info", "No file selected.")'''
        
    def configure_color_scheme(self):
        # Function to configure color scheme
        primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
        off_color = colorchooser.askcolor(title="Choose Off Color")[1]

        # Apply the chosen colors to the GUI
        self.main.configure(bg=primary_color)
        self.label.configure(bg=primary_color)
        self.code_text.configure(bg=off_color)
        self.operations_text.configure(bg=off_color)

    def operations_output(self, op, func_name, operand):
        # output accumulator value in gui
        output = f'Performed op {op}: {func_name} with operand {operand}\n'
        self.operations_text.insert(tk.END, output)

    def final_output(self):
        # output accumulator value in gui
        output = f"Final accumulator value: {self.sim._accumulator}\n"
        self.operations_text.insert(tk.END, output)
        messagebox.showinfo("Result: ", f"Final Accumulator Value: {self.sim._accumulator}") 
    
    def destroy_program(self):
        # close the main window
        self.main.destroy()

    def read(self):
        #Read a word from the keyboard into memory
        entry_window = tk.Toplevel(self.main)  # create user input window
        entry_window.title("Enter Value")
        entry_window.geometry("300x100")

        def submit():
            try:
                value = int(entry.get())  #check for int
                self.memory.truncate(value)  #truncate if the user value exceeds 4 digits
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
        messagebox.showinfo("Write Operation", f"Value at memory location {self.sim._operand}: {value}")

    def too_long(self):
        # gui error message if sim pc exceeds available memory
        messagebox.showerror("Error", "Program too long.")
