import threading
import os
import time

import Pause

def action(alarm):
   os.system(str(alarm))
   print "TIME IS UP ! \n"

def get_duration(time):
    seconds = 0
    #check the format

    time = time.split(" ")
    str_len = len(time)
    if (str_len == 2):
        #print "minutes and seconds"
        if(time[0][-1] != 'm' or time[1][-1] != 's'):
            print "wrong format"
            return -1
        else:
            if(time[0][:-1].isdigit() == False or time[1][:-1].isdigit() == False):
                #print "wrong format"
                return -1
            seconds = 60*int(time[0][:-1]) + int(time[1][:-1])
        
    elif(str_len == 1):
        time = str(time[0])
        #print "minutes or seconds only"
        if(time[-1] != 'm' and time[-1] != 's'):
            if(time.isdigit() == False):
                print "wrong format"
                return -1
        if(time[-1] == 'm'):
            if(time[:-1].isdigit() == False):
                print "wrong format"
                return -1
            else:
                seconds = 60*int(time[:-1])
        elif(time[-1] == 's'):
            if(time[:-1].isdigit() == False):
                print "wrong format"
                return -1
            else:
                seconds = int(time[:-1])
        else:
            seconds = int(time)
        
    else:
        print "wrong format"
        return -1
    
    return seconds



def start_timer():
   print "Provide a duration in Xm Ys format (example: 12m 50s):\n", 
   duration = get_duration(raw_input());
   while(duration == -1):
      print "Provide a duration in Xm Ys format (example: 12m 50s):\n", 
      duration = get_duration(raw_input());
   alarm = "C:\Users\JW2\Desktop\Python\Timer\siren-alarm.mp3"
   tim = threading.Timer(duration, action, [alarm])
    
   tim.start()
   external_clock = time.clock()

   while(Pause.wait_for_pause(duration) != 0):
      duration = duration - (time.clock() - external_clock)
      tim.cancel()
      
      Pause.wait_for_unpause()
      tim = threading.Timer(duration, action, [alarm])
      tim.start()
      external_clock = time.clock() #"reset" the clock
    
start_timer()
