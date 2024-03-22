import pytest
from main import *
from execute_program import *
from uvsim import *
from GUI_layout import *
from GUI_actions import *

def test_always_passes():
    assert True

# def test_always_fail():
#     assert False
   
def test_load():
    my_memory = Memory(100)
    my_memory.store(0, 10)
    accumulator = my_memory.load(0)
    assert accumulator == 10

def test_neg_load():
    my_Sim = Memory(100)
    my_Sim.store(0, -5)
    accumulator = my_Sim.load(0)
    assert accumulator == -5
    
def test_store():
    my_Sim = Memory(100)
    my_Sim.store(5, 50)
    storing = my_Sim.load(5)
    assert storing == 50

def test_neg_store():
    my_Sim = Memory(100)
    my_Sim.store(0, -10)
    my_Sim.store(0, -50)
    storing = my_Sim.load(0)
    assert storing == -50

def test_multiply():
    a = 5
    b = 10
    my_sim = UVSim()
    result = my_sim.multiply(a, b)
    assert result == 50

def test_neg_multiply():
    a = -5
    b = 10
    my_sim = UVSim()
    result = my_sim.multiply(a, b)
    assert result == -50
    
def test_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    b = 5
    result = my_Sim.divide(my_Sim.get_accumulator(), b)
    assert result == 2

def test_zero_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(10)
    b = 0
    result = my_Sim.divide(my_Sim.get_accumulator(), b)
    assert result == 10

def test_neg_divide():
    my_Sim = UVSim()
    my_Sim.set_accumulator(-10)
    b = 5
    result = my_Sim.divide(my_Sim.get_accumulator(), b)
    assert result == -2

def test_divide_less_one():
    my_Sim = UVSim()
    my_Sim.set_accumulator(1)
    b = 5
    result = my_Sim.divide(my_Sim.get_accumulator(), b)
    assert result == 0
    
def test_branch():
    my_Sim = UVSim()
    my_Sim.set_operand(5)
    result = my_Sim.branch(my_Sim.get_operand())
    assert result == 5
    
def test_branch2():
    my_Sim = UVSim()
    my_Sim.branch(10)
    my_Sim.set_operand(15)
    result = my_Sim.branch(my_Sim.get_operand())
    assert result == 15
        
def test_branchNeg():
    my_Sim = UVSim()
    my_Sim.set_operand(20)
    my_Sim.set_accumulator(-5)
    result = my_Sim.branch_neg(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 20
    
def test_branchNeg2():
    my_Sim = UVSim()
    my_Sim.set_operand(5)
    my_Sim.set_accumulator(5)
    result = my_Sim.branch_neg(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 1

def test_branchZero():
    my_Sim = UVSim()
    my_Sim.set_operand(25)
    my_Sim.branch(5)
    result = my_Sim.branch_zero(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 25
    
def test_branchZero2():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    result = my_Sim.branch_zero(my_Sim.get_accumulator(), my_Sim.get_operand(), my_Sim.get_pc())
    assert result == 1
    
def test_add():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    b = 5
    result = my_Sim.add(my_Sim.get_accumulator(), b)
    assert result == 10

def test_add2():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    my_memory = Memory(100)
    my_Sim.set_program([3005, 4300, 0000, 0000, 0000, 5])
    my_memory.load_program(my_Sim.get_program())
    Execute.execute_program(my_Sim, GUIActions(my_Sim, my_memory), my_memory)
    result = my_Sim.get_accumulator()
    assert result == 10
    
def test_subtract():
    my_Sim = UVSim()
    my_Sim.set_accumulator(5)
    b = 10
    result = my_Sim.subtract(b, my_Sim.get_accumulator())
    assert result == 5
    
def test_subtract2():
    my_Sim = UVSim()
    my_memory = Memory(100)
    my_Sim.set_accumulator(10)
    my_Sim.set_program([3105, 4300, 0000, 0000, 0000, 5])
    my_memory.load_program(my_Sim.get_program())
    Execute.execute_program(my_Sim, GUIActions(my_Sim, my_memory), my_memory)
    result = my_Sim.get_accumulator()
    assert result == 5
    
def test_execute_my_Sim():
    my_Sim = UVSim()
    my_memory = Memory(100)
    my_Sim.set_program([2006, 3006, 3106, 3006, 4300, 0000, 5])
    my_memory.load_program(my_Sim.get_program())
    Execute.execute_program(my_Sim, GUIActions(my_Sim, my_memory), my_memory)
    result = my_Sim.get_accumulator()
    assert result == 10

def test_execute_my_Sim2():
    my_Sim = UVSim()
    my_memory = Memory(100)
    my_Sim.set_program([2005, 3110, 4300, 0000, 0000, 10, 0000, 0000, 0000, 0000, 5])
    my_memory.load_program(my_Sim.get_program())
    Execute.execute_program(my_Sim, GUIActions(my_Sim, my_memory), my_memory)         
    result = my_Sim.get_accumulator()
    assert result == 5
