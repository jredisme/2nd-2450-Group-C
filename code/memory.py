class Memory():
    '''Memory class, handles memory-related operations'''
    def __init__(self, size=100):
        self._registers = [0] * size
    
    def load(self, operand):
        # load a word from memory into the accumulator
        return self._registers[operand]
      
    def store(self, operand, accumulator):
        # store a word from the accuulator into memory
        self._registers[operand] = accumulator
      
    def load_program(self, program):
        # load a program into memory
        for i, instruction in enumerate(program):
            self._registers[i] = self.truncate(instruction)  # avoid overflow
    
    def truncate(self, value):
        # truncate value to six digits to avoid overflow when needed  
        if value > 999999:
            value %= 1000000
        elif value < -999999:
            value = -value
            value %= 1000000
            value = -value
        return value
    
    def len(self):
        # return length of registers list
        return len(self._registers)
    
    def clear(self):
        # clear memory
        self._registers = [0] * self.len()
