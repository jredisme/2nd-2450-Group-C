from uvsim import UVSim
from GUI import SimpleGUI
from memory import Memory

def main():
    '''Run machine language simulator'''
    
    my_sim = UVSim()  # initialize simulator
    my_memory = Memory(100)  # initialize Memory object with 100 registers  
    my_gui = SimpleGUI(my_sim, my_memory) # intialize gui, pass sim and memory to gui
    my_gui.main.mainloop() #loops through GUI operations while GUi is open

if __name__ == "__main__":
    main()
    
