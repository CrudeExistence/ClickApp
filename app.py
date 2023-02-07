import tkinter as tk
import time
import threading
from PIL import Image, ImageTk

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

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)


#! - layout plan indicator
#todo - Do I want a logo? Yes
# Logo
logo = Image.open('assets\LgoPrintFultest.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#! info
intro = tk.Label(text="Welcome to the ClickApp Auto Click Bot! \n\nCurrent delay setting for the click function is: {} seconds between clicks \n\nIn order to Start/Stop the Auto Click function- \n-Press the {} key \n\nIn order to change the speed- \n-Press the {} key \n\nTo exit the program- \n-Press the {} key \n\nEnjoy!".format(delay,start_stop_key,change_speed_key,exit_key))
intro.grid(column=1, row=1)

#* Function for start/stop button
def clicker():
    ss_text.set("Stop")
    print('is this working??')

#! start/stop button
    #* raised = stopped / sunken = running
ss_text = tk.StringVar()
start_stop = tk.Button(
    window,
    textvariable=ss_text,
    command=lambda:clicker(),
    width=15,
    height=2,
    bg="black",
    fg="blue",
    pady=15,
    relief=tk.RAISED
)
ss_text.set("Start")
start_stop.grid(column=1, row=2)


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
# outro = tk.Label(text="~~ Created by CrudeExistence")
# outro.grid(column=,row=)

window.mainloop()