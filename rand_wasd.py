from icecream import ic
import os
import time
from datetime import datetime
import logging
import pyautogui
import random
import sys
import ctypes

#icecream status
#ic.enable()
#ic.disable()

#remove last log file
os.remove("rand_wasd.log")

#timestamp for script run
runtimestamp=datetime.now()
runtlog=runtimestamp.strftime("%m/%d/%Y %I:%M:%S %p")

#setup logging
logging.basicConfig(filename="rand_wasd.log", filemode="a")
logger = logging.getLogger("rand_wasd")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)-12s %(levelname) -8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
logger.info(f' {tlog} - Starting script...')

keylist=('w','a','s','d','s','s','d')
rand1=random.randrange(1,20)
rand2=random.randrange(1,10)

ic.disable()
#pyautogui.press('left')  
ic('\n')
ic(random.randrange(1,20))
ic(random.uniform(1,20))
ic(random.randrange(1,20))
ic(random.randrange(1,20))
ic()
ic.enable()
#timelimit seconds*minutes*hours
timelimit=(60.00*60*3)

seconds=0
time.sleep(2)
try:
    while seconds < (timelimit):
        randchoice=random.choice(keylist)
        ic(f"random choice {randchoice}")
        pyautogui.keyDown(randchoice)
        #pyautogui.press(randchoice)
        
        
        randpress=random.uniform(1.00,8.00)
        ic(f"random press {randpress}")
        time.sleep(randpress)
        seconds = seconds + randpress
        
        
        pyautogui.keyUp(randchoice)
        
        randwait=random.uniform(1.00,5.00)
        ic(f"random wait {randwait}")
        time.sleep(randwait)
        seconds = seconds + randwait
             
        logger.info(ic(f"random choice {randchoice}"))
        logger.info(ic(f"random press {randpress}"))
        logger.info(ic(f"random wait {randwait}"))
        del randchoice
        del randpress
        del randwait
except Exception as e:
    logger.warning(f'{e}')
    MB_SETFOREGROUND = 0x10000
    ctypes.windll.user32.MessageBoxW(0, "Script Fail Safe has been enabled", "Fail Safe Notification", MB_SETFOREGROUND)
    sys.exit()
        
ic("loop has finished")    
timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
MB_SETFOREGROUND = 0x10000
ctypes.windll.user32.MessageBoxW(0, f' {tlog} App has reached is maximum time limit of {timelimit} seconds', "Completion Notification", MB_SETFOREGROUND)
logger.info(f' {tlog} App has reached is maximum time limit of {timelimit} seconds')