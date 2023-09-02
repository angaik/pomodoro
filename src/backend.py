import time
# playsound==1.2.2 module version
import playsound as ps
 
# time.gmtime() returns a struct similar/same to datetime structs. 
# Seems I can set up a timer without datetime module!

# Core timer function for playing alarm tone after specific time delay.
def timer(waiting_secs:int):
    """Timer function to play alarm tones with user-input delay in seconds."""
    
    # time.time(): Time since UNIX Epoch in seconds (float output)
    # time.time() returns time in seconds. Thus, e.g. to set the next time point
    # for 2 minutes, add 120.
    print(time.gmtime(time.time()))
    time.sleep(waiting_secs)
    print(time.gmtime(time.time()))
    ps.playsound("../audio/mixkit-rooster-crowing-in-the-morning\
                 -2462.wav")

# TODO: Refactor after learning basic GUI in python to link functions with 
# GUI buttons.
def work_time(time_in_secs:int):
    timer(time_in_secs)

def short_break(time_in_secs:int):
    timer(time_in_secs)

def long_break(time_in_secs:int):
    timer(time_in_secs)

work_time_secs = 20*60
short_break_secs = 5*60
long_break_secs = 15*60