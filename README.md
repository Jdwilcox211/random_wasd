# random_wasd
This script randomly presses w,a,s, or d keys to stop the game from disconnecting due to being idle.
Could be used on many games but was developed to use with Fortnite. Some games may require more robust methods so it may not work for all.

Must have python installed https://www.python.org/
was created with 3.11.4, and successfully tested on 3.12.3

Install requirements.txt
Syntax to install requirements: pip install -r *path*/requirements.txt

you will have to edit the paths in .bat for your own python paths and script directory. if you choose to use the bat



time limit default to run for 3 hours.  timelimit variable is on line 17 of the rand_wasd.py script
timelimit variable is formatted as seconds x minutes x hours. ie .60.00*60*3 is 3 hours.  
Keep one number in the variable a float (include decimals ie60.00)

If you wish to stop early move cursor to the top left corner of the screen on the main monitor and hold until the fail safe popup appears.

This script logs each run and deletes the previous log before running again.

if you wish to add keys other than wasd or change the weight of each key to be chosen you can add keys to the keylist variable on line 43


Script functions by picking the number of random button presses and push and wait times to make up the total timelimit.  It then iterates the button presses until complete or fail safe is triggered.