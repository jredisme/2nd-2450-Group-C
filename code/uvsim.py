class UVSim():
    '''The UVSim class simulates a basic machine and defines machine language operations.
    Operations include loading a program into memory, load/store, math, branch, halt'''
    def __init__(self):
        self._accumulator = 0  # results of various operations are stored in accumualtor  
        self._pc = 0  # program counter
        self._operand = 0
        self._op = 0

    def add(self, a, b):
        # add a word from memory to a word in the accumulator
        return (a + b)
    
    def subtract(self, a, b):
        # subtrat a word from memory from a word in the accumulator
        return (a - b)
    
    def divide(self, a, b):
        # divide a word in the accumulator by a word from memory
        if b == 0:
            return a
        return (a // b)
    
    def multiply(self, a, b):
        # multiply a word from meory by a word in the accumulator
        return (a * b)
      
    def branch(self, operand):
        # branch to a specific location in memory
        return operand
    
    def branch_neg(self, accumulator, operand, pc):
        # branch to a location in memroy if the accumulator is negative
        
        if accumulator < 0:
            return operand
        else:
            return pc + 1
        
    def branch_zero(self, accumulator, operand, pc):
        # branch to a location in memroy if the accumulator is 0
        if accumulator == 0:
            return operand
        else:
            return pc + 1
          
    def halt(self):
        # stop the program
        return True
    
    def get_accumulator(self):
        return self._accumulator
    
    def set_accumulator(self, value):
        self._accumulator = value
        
    def set_operand(self, value):
        self._operand = value
    
    def get_operand(self):
        return self._operand
        
    def set_memory(self, index, value):
        self._memory[index] = value
        
    def set_program(self, program):
        self._program = program
        
    def get_program(self):
        return self._program
    
    def get_pc(self):
        return self._pc
        
