class Process:
    '''This class reads a program from a data source.
    It also loads the program into memory'''
    
    def read_txt(file_path):
        #read a program from a file.
        #return it as a list of instructions and data values
        program = []
        with open(file_path, 'r') as file:
            for line in file:
                program.append(line)  # add each line of program to program, check for int
        return program
       
