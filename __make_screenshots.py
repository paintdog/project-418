import pyscreeze
import time

while True:
    time.sleep(0.2)
    
    lt = time.localtime()
    new_file = time.strftime("%Y-%m-%d %H-%M-%S", lt) + ".png"

    image = pyscreeze.screenshot(new_file)
