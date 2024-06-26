UVSIM 

- This program is a simple interpreter for a language called BasicML. BasicML is a simple language that includes operations like read, write, load, store, add, subtract, multiply, divide, branch, branchNeg, and branchZero.

How to Open

Running Python Program in VS Code

Open VS Code
- Press the Windows key, type "Visual Studio Code", and press Enter.

Change Directory in Terminal
- Open a new terminal in VS Code (`Terminal > New Terminal`).
- Type `cd 'your_directory_path'` to change the directory.

Run Python Program
- In the terminal, type `python your_file.py` to run your program.

Replace `'your_directory_path'` and `'your_file.py'` with your actual directory path and Python file name.

How to Use
- Run the program. A graphical user interface window will pop up. You will be prompted to select a file to run. By selecting, "File" from the toolbar a drop down menu will appear. Select "Open" this will open the computer's directory allowing you to select a file. This file should contain your BasicML program. Each line of the file should contain a four-digit integer.

- If the file is found, the program will read the commands from the file after clicking "Run" from the same drop down menu. Each command should be a 4-digit number. The first two digits are the operation code (op), and the last two digits are the operand.

- If a command is more than 4 digits, or if the operation code is not a valid operation code, the program will raise an error and stop execution. Valid operation codes are 10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43(see bottom for description)

- If the operation code is 10 (READ), the program will open another window and prompt you to enter a number into the input box below in order to read into the specified location. Once entered, click the, "Submit" button.

- After all commands have been read and processed, the program will execute the BasicML program.

- The result of the program will appear in the original window's output text box.

- Write and save code. In the top text box you can write your own machine code or edit other code you've already loaded in. The code must be written with a "+" followed by 4-6 digits, repeat this for each line of code. Once you've written or changed code in the top text box, go to the toolbar and select "Save Code Block". As long as code is in basicML you'll be able to name the file and save it. 

- Configure color scheme. From the toolbar select, "Configure Color Scheme". A color wheel will appear. Click any color on the color wheel then select "ok" in the same box to change the window's primary color. The window will close and open a new one. Click anywhere on the color wheel to select the window's off color and then select "ok". The GUI window's colors should now change to what you've selected.

- Open a new window. From the toolbar select, "Open New". This opens another GUI window.

Input File Format
- The input file should contain one command per line. Each command should be a 4 or 6-digit number. For 4-digit numbers, the first two digits are the operation code, and the last two digits are the operand. The file must end with the 4300 Halt Command. For 6-digit numbers, the first three digits are for the operation code (since operation codes are only digits, a “0” will be the first digit) and the last three are the operand. The file must end with the 043000 Halt Command. 

Here's an example of what an input file might look like:
- +1007
- +2007
- +3008
- +021009
- +1010
- +011010
- +4300

Here's what that above file does:
- 1007: This is a READ operation. The program will prompt the user to enter a number, which will be stored in memory location 07.

- 2007: This is a LOAD operation. The program will load the value from memory location 07 into the accumulator.

- 3008: This is an ADD operation. The program will add the value at memory location 08 to the value in the accumulator, storing the result in the accumulator.

- 021009: This is a STORE operation. The program will store the value currently in the accumulator to memory location 09.

- 1010: This is another READ operation. The program will prompt the user to enter another number, which will be stored in memory location 10.

- 011010: This is a WRITE operation. The program will print the value at memory location 10.

- 4300: This is a HALT operation. The program will stop executing.


Error Handling
- If the operation code is not a valid operation code, the program will raise an error and stop execution. The error message will indicate the problem and ask you to correct the file.

Operands Description:
- 10 (READ): This operation code prompts the user to enter a number, which is then stored in a specific location in memory. The location is specified by the operand.

- 11 (WRITE): This operation code prints the value at a specific location in memory. The location is specified by the operand.

- 20 (LOAD): This operation code loads the value from a specific location in memory into the accumulator. The location is specified by the operand.

- 21 (STORE): This operation code stores the value currently in the accumulator to a specific location in memory. The location is specified by the operand.

- 30 (ADD): This operation code adds the value at a specific location in memory to the value in the accumulator, storing the result in the accumulator. The location is specified by the operand.

- 31 (SUBTRACT): This operation code subtracts the value at a specific location in memory from the value in the accumulator, storing the result in the accumulator. The location is specified by the operand.

- 32 (DIVIDE): This operation code divides the value in the accumulator by the value at a specific location in memory, storing the result in the accumulator. The location is specified by the operand.

- 33 (MULTIPLY): This operation code multiplies the value in the accumulator by the value at a specific location in memory, storing the result in the accumulator. The location is specified by the operand.

- 40 (BRANCH): This operation code changes the program counter to the location specified by the operand, effectively causing the program to "jump" to a different part of the program.

- 41 (BRANCHNEG): This operation code checks if the value in the accumulator is negative. If it is, it changes the program counter to the location specified by the operand, causing the program to "jump" to a different part of the program.

- 42 (BRANCHZERO): This operation code checks if the value in the accumulator is zero. If it is, it changes the program counter to the location specified by the operand, causing the program to "jump" to a different part of the program.

- 43 (HALT): This operation code stops the execution of the program. It does not require an operand.
