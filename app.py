import tkinter as tk
import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#initialize tk(gui) as window and assign a title
window = tk.Tk()
window.title("Crude Auto Clicker")

delay = 0.31
button = Button.left
start_stop_key = KeyCode(char=']')
exit_key = KeyCode(char=';')
change_speed_key = KeyCode(char='[')

#! - layout plan indicator
#! info
intro = tk.Label(text="Welcome to the ClickApp Auto Click Bot! \n\nCurrent delay setting for the click function is: {} seconds between clicks \n\nIn order to Start/Stop the Auto Click function- \n-Press the {} key \n\nIn order to change the speed- \n-Press the {} key \n\nTo exit the program- \n-Press the {} key \n\nEnjoy!".format(delay,start_stop_key,change_speed_key,exit_key))
intro.pack()


#! start/stop button
    #* raised = stopped / sunken = running
start_stop = tk.Button(
    text="start/stop",
    width=20,
    height=20,
    bg="black",
    fg="blue",
    relief=tk.RAISED
)

start_stop.pack()

#! assigned increase speed keyboard button
    #* most likely flat design
#! reassign text field
    #* reassign submit button
#! increase speed button

#! current speed
    #* flat design to display speed

#! assigned increase speed keyboard button
    #* most likely flat design
#! reassign text field
    #* reassign submit button
#! decrease speed button

#! Created by CrudeExistence
outro = tk.Label(text="~~ Created by CrudeExistence")
outro.pack()

window.mainloop()