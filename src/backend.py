import time
# playsound==1.2.2 module version
import playsound as ps
import functools as fn
import typing

# time.gmtime() returns a struct similar/same to datetime structs. 
# Seems I can set up a timer without datetime module!

# Core timer function for playing alarm tone after specific time delay.
def timer(waiting_secs:int):
    """Timer function to print timestamps & play alarm tone with user-input
    delay in seconds."""
    # time.time(): Time since UNIX Epoch in seconds (float output)
    # time.time() returns time in seconds. Thus, e.g. to set the next time point
    # for 2 minutes, add 120.
    print(time.gmtime(time.time()))
    time.sleep(waiting_secs)
    print(time.gmtime(time.time()))
    ps.playsound("../audio/mixkit-rooster-crowing-in-the-morning-2462.wav")

def assemble_timers(
        work_time_secs = 20*60,
        short_break_secs = 5*60,
        long_break_secs = 15*60
    ):

    work_time = fn.partial(timer,work_time_secs)
    short_break = fn.partial(timer,short_break_secs)
    long_break = fn.partial(timer,long_break_secs)

    def assemble_timer(button_text:str,timer_func:typing.Callable,anchor:str):
        return {"text":button_text,
                "command":timer_func,
                "anchor":anchor}

    # Assembled dicts
    return [assemble_timer("Start work time",work_time,'n'),
        assemble_timer("Start short break",short_break,'w'),
        assemble_timer("Start long break",long_break,'e')]