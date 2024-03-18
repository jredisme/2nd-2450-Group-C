class Execute:
    '''This class simulates basic machine language operations and executes them'''
    def execute_program(sim, gui, memory):
        # Executes the program
        # Takes a sim, gui, and memory as parameters
            # The sim performs arithmetic, branch, and half operations, and keeps track of pc
            # The gui performs input/output operations
            # Memory performs load/store operations and truncate to avoid overflow

        sim._pc = 0
        while sim._pc < memory.len():
            sim._op = memory._registers[sim._pc] // 100
            sim._operand = memory._registers[sim._pc] % 100
            match sim._op:
                case 10: #read
                    gui.read() #front end function
                case 11: #write
                    gui.write() #front end function
                case 20: #load
                    sim._accumulator = memory.load(sim._operand)  #memory function
                case 21: #store
                    memory.store(sim._operand, sim._accumulator)  #memory function
                case 30: #add
                    sim._accumulator = memory.truncate(sim.add(sim._accumulator, memory.load(sim._operand)))
                case 31: #subtract
                    sim._accumulator = memory.truncate(sim.subtract(sim._accumulator, memory.load(sim._operand)))
                case 32: #divide
                    sim._accumulator = memory.truncate(sim.divide(sim._accumulator, memory.load(sim._operand)))
                case 33: #multiply
                    sim._accumulator = memory.truncate(sim.multiply(sim._accumulator, memory.load(sim._operand)))
                case 40: #branch
                    sim._pc = sim.branch(sim._operand)
                case 41: #branch_neg
                    sim._pc = sim.branch_neg(sim._accumulator, sim._operand, sim._pc)
                case 42: #branch_zero
                    sim._pc = sim.branch_zero(sim._accumulator, sim._operand, sim._pc)
                case 43: #halt
                    my_bool = sim.halt()
                    if my_bool:
                        break
            if sim._op not in (40, 41, 42):  # if not a branch op
                sim._pc += 1
        if sim._pc > 99:
            gui.too_long() #front end function
