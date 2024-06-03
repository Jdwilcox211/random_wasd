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
ic.disable()

#timelimit for script to run seconds*minutes*hours.  60.00*60*3 is 3 hours.  keep one variable a float
timelimit=(60.00*60*3)

#remove last log file
try:
    os.remove("rand_wasd.log")
except Exception as e:
    ic(e)
    
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

#define list and variables
#keylist is keys to press, loop will select a random entry from teh list
keylist=('w','a','s','d','s','s','d')
#defining list to fill with random entries
randkeylist = []
randpresslist = []
randwaitlist = []
#seconds is the starting seconds 0 at which to add the random press and wait times to.  this will be compared to the timelimit variable to ensure it runs for exact time limit and no longer
seconds=0
#timeran to calculate runtime through out script
runtime=0
time.sleep(5)

try:
    while seconds < (timelimit):
        #pick random key add to list
        randchoice=random.choice(keylist)
        ic(f"random choice {randchoice}")
        randkeylist.append(randchoice)
        
        #pick random press time for button and add to list.
        randpress=random.uniform(1.00,8.00)
        ic(f"random press {randpress}")
        randpresslist.append(randpress)
        seconds = seconds + randpress
    
        #pick random wait time for inbetween button pushes and add to list.     
        randwait=random.uniform(1.00,5.00)
        ic(f"random wait {randwait}")
        randwaitlist.append(randwait)
        seconds = seconds + randwait
        
        
        del randchoice
        del randpress
        del randwait
        
        
    logger.info(ic(f"random choice: {randkeylist} \n \n"))
    logger.info(ic(f"random press: {randpresslist} \n \n"))
    logger.info(ic(f"random wait: {randwaitlist} \n \n \n"))
    logger.info(ic(f"TOTAL List Entries: {len(randkeylist)} \n \n \n"))        
    
    #loop to interate tthe entrys from the lists
    for i in range(0,len(randkeylist)):
        
        logger.info(ic(f"random key choice {randkeylist[i]}"))
        pyautogui.keyDown(randkeylist[i])
        logger.info(ic(f"random press {randpresslist[i]}"))
        time.sleep(randpresslist[i])
        pyautogui.keyUp(randkeylist[i])
        logger.info(ic(f"random wait {randwaitlist[i]} \n "))
        time.sleep(randwaitlist[i])
        runtime = runtime + randwaitlist[i] + randpresslist[i]
        
        logger.info(ic(f"Total Hours ran {(int(((runtime)/60)/60))}"))
        logger.info(ic(f"Total Minutes ran {int((runtime)/60)}"))
        logger.info(ic(f"Total Seconds ran {int(runtime)} \n \n \n"))
        
            
except Exception as e:
    logger.warning(f'{e}')
    MB_SETFOREGROUND = 0x10000
    ctypes.windll.user32.MessageBoxW(0, "Script Fail Safe has been enabled", "Fail Safe Notification", MB_SETFOREGROUND)
    sys.exit()
        
               
ic("loop has finished")    
timestamp=datetime.now()
tlog=timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
MB_SETFOREGROUND = 0x10000
ctypes.windll.user32.MessageBoxW(0, f' {tlog} App has reached the maximum time limit of {timelimit} seconds', "Completion Notification", MB_SETFOREGROUND)
logger.info(f' {tlog} App has reached is maximum time limit of {timelimit} seconds')