import tkinter as tk
import time
import threading
from PIL import Image, ImageTk

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#initialize tk(gui) as window and assign a title
window = tk.Tk()
window.title("Crude Auto Clicker")

#Set minimum size of the window (x, y)
window.minsize(600,450)

delay = 0.31
button = Button.left
ss_button = ']'
start_stop_key = KeyCode(char=ss_button)
exit_button = ';'
exit_key = KeyCode(char=exit_button)
change_speed_button = '['
change_speed_key = KeyCode(char=change_speed_button)
temp_start_stop = ''
temp_exit_key = ''
temp_speed_key = ''

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        window.destroy()

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def speed_change():
    delay_text.set("The current speed is: " + str(click_thread.delay))

#? clicking part of program with listener application
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            click_thread.delay = 0.31
            delay_text.set("The current speed is: " + str(click_thread.delay))
        else:
            click_thread.start_clicking()
    elif key == change_speed_key:
        if click_thread.running:
            if click_thread.delay == 0.31:
                click_thread.delay = 0.01
                delay_text.set("The current speed is: " + str(click_thread.delay))
            elif click_thread.delay == 0.01:
                click_thread.delay = 0.0009
                delay_text.set("The current speed is: " + str(click_thread.delay))
            elif click_thread.delay == 0.0009:
                click_thread.delay = 0.31
                delay_text.set("The current speed is: " + str(click_thread.delay))
        else:
            #! Need to change to alert of some kind
            print("clicker isn't running")
    elif key == exit_key:
        click_thread.exit()

        

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=4)


#! - layout plan indicator
# Logo row 0
logo = Image.open('assets\LgoPrintFultest.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Running indicator row 0 - indicator needs two different labels - can't duplicate
indication_text = tk.StringVar()
indication = tk.Label(
    textvariable=indication_text,
    width=10,
    height=2,
    bg="red",
    fg="black",
    pady=15,
    relief=tk.GROOVE
)
indication2 = tk.Label(
    textvariable=indication_text,
    width=10,
    height=2,
    bg="red",
    fg="black",
    pady=15,
    relief=tk.RIDGE
)
indication_text.set("Stopped")
indication.grid(column=0,row=0)
indication2.grid(column=2,row=0)


#! info
# intro = tk.Label(text="Welcome to the ClickApp Auto Click Bot! \n\nCurrent delay setting for the click function is: {} seconds between clicks \n\nIn order to Start/Stop the Auto Click function- \n-Press the {} key \n\nIn order to change the speed- \n-Press the {} key \n\nTo exit the program- \n-Press the {} key \n\nEnjoy!".format(delay,start_stop_key,change_speed_key,exit_key))
# intro.grid(column=1, row=1)

#* Function for start/stop button
# def clicker():
#     ss_text.set("Stop")
#     print('is this working??')

#! start/stop button
    #* raised = stopped / sunken = running
# ss_text = tk.StringVar()
# start_stop = tk.Button(
#     window,
#     textvariable=ss_text,
#     command=lambda:clicker(),
#     width=15,
#     height=2,
#     bg="black",
#     fg="blue",
#     pady=15,
#     relief=tk.RAISED
# )
# ss_text.set("Start")
# start_stop.grid(column=1, row=2)

delay_text = tk.StringVar()
current_speed = tk.Label(
    textvariable=delay_text
)
delay_text.set("The current speed is: " + str(click_thread.delay))
current_speed.grid(column=1,row=1)

#! assigned increase speed keyboard button
    #* most likely flat design
speed_info = tk.Label(
    text=""
)

#! reassign text field
    #* reassign submit button
#! increase speed submit button

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

#? Exit function works to button. Now to assign button listener for exit.
def exit():
    click_thread.exit()

test_exit = tk.Button(
    window,
    text="exit",
    command=lambda:exit(),
    relief=tk.RAISED
)
test_exit.grid(column=1, row=3)

with Listener(on_press=on_press) as listener:
    window.mainloop()
    # listener.start()
    # listener.join()
    # listener.stop()
