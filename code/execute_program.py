class Execute:
    '''This class simulates basic machine language operations and executes them'''
    def execute_program(sim, gui):
        # Executes the program
        # Takes a sim, gui, and memory as parameters
            # The sim performs arithmetic, branch, and half operations, and keeps track of pc
            # The gui performs input/output operations
            # Memory performs load/store operations and truncate to avoid overflow

        sim._pc = 0
        while sim._pc < gui.memory.len():
            sim._op = gui.memory._registers[sim._pc] // 100
            sim._operand = gui.memory._registers[sim._pc] % 100
            func_name = ''
            if sim._pc > 99:
                gui.too_long()  
            match sim._op:
                case 10: #read
                    gui.read() #front end function
                    func_name = 'read'
                case 11: #write
                    gui.write(gui.memory.load(sim._operand), sim._operand) #front end function
                    func_name = 'write'
                case 20: #load
                    sim._accumulator = gui.memory.load(sim._operand)  #memory function
                    func_name = 'load'
                case 21: #store
                    gui.memory.store(sim._operand, sim._accumulator)  #memory function
                    func_name = 'store'
                case 30: #add
                    sim._accumulator = gui.memory.truncate(sim.add(sim._accumulator, gui.memory.load(sim._operand)))
                    func_name = 'add'
                case 31: #subtract
                    sim._accumulator = gui.memory.truncate(sim.subtract(sim._accumulator, gui.memory.load(sim._operand)))
                    func_name = 'subtract'
                case 32: #divide
                    sim._accumulator = gui.memory.truncate(sim.divide(sim._accumulator, gui.memory.load(sim._operand)))
                    func_name = 'divide'
                case 33: #multiply
                    sim._accumulator = gui.memory.truncate(sim.multiply(sim._accumulator, gui.memory.load(sim._operand)))
                    func_name = 'multiply'
                case 40: #branch
                    sim._pc = sim.branch(sim._operand)
                    func_name = 'branch'
                case 41: #branch_neg
                    sim._pc = sim.branch_neg(sim._accumulator, sim._operand, sim._pc)
                    func_name = 'branch neg'
                case 42: #branch_zero
                    sim._pc = sim.branch_zero(sim._accumulator, sim._operand, sim._pc)
                    func_name = 'branch zero'
                case 43: #halt
                    my_bool = sim.halt()
                    func_name = 'halt'
                    if my_bool:
                        return
            # if sim._op in (10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 32, 43):
            #     gui.operations_output(sim._op, func_name, sim._operand)
            if sim._op not in (40, 41, 42):  # if not a branch op
                sim._pc += 1
