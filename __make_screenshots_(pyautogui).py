import pyscreeze
import time
import pyautogui
import pymsgbox


pages = 324         # User input required...


pymsgbox.alert('Can we start?', 'Info')
time.sleep(4)

for page in range(pages):
    lt = time.localtime()
    new_file = time.strftime("%Y-%m-%d %H-%M-%S", lt) + ".png"
    image = pyscreeze.screenshot(new_file)
    pyautogui.typewrite(['right'])
    time.sleep(2)

pymsgbox.alert("I've finished.", 'Info')    
