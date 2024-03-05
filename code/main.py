from uvsim import UVSim
from GUI import SimpleGUI

def main():
    '''Run machine language simulator'''
    my_sim = UVSim(100)  # initialize simulator with 100 memory registers
    my_gui = SimpleGUI(my_sim) # intialize gui, pass sim to gui
    my_gui.main.mainloop() #loops through GUI operations while GUi is open


if __name__ == "__main__":
    main()
    
