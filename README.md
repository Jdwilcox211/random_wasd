# random_wasd

This script randomly presses w,a,s, or d keys to stop the game from sensing you're idle.  
Could be used on many games but was developed to use with Fortnite.  Some games may require more robust methods so it may not work for all.

Must have python installed https://www.python.org/
was created with 3.11.4, will likely work on later installations.

you will have to edit the paths in .bat for your own python paths and script directory.
you can set runtime in the rand_wasd.py script around line 17. The variable name is timelimit.  
It is set to run for seconds X minutes X hours.  60.00 X 60 X 3 is 3 hours.  Keep one variable a float (with decimal point) important to calculate rand time increments.

this is intended to be used as separate bats and linked to a hotkey or stream deck.  I use a free app that turns my phone and/or tablet into a stream deck.  Touch Portal, pro version very affordable also. https://www.touch-portal.com/
