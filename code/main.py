from uvsim import UVSim
from memory import Memory
from GUI_actions import GUIActions

def main():
    '''Run machine language simulator'''
    
    my_sim = UVSim()  # initialize simulator
    my_memory = Memory(100)  # initialize Memory object with 100 registers  
    my_gui = GUIActions(my_sim, my_memory) # perform GUI actions
    my_gui.main.mainloop() #loops through GUI operations while GUi is open

if __name__ == "__main__":
    main()
    
