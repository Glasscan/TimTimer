import threading
import os
import time

import Pause
import setDefault

def action(alarm):
   os.system(str(alarm))
   print ("TIME IS UP ! \n")

def get_duration(time):
    seconds = 0
    #check the format

    time = time.split(" ")
    str_len = len(time)
    if (str_len == 2):
        #print ("minutes and seconds")
        if(time[0][-1] != 'm' or time[1][-1] != 's'):
            print ("wrong format")
            return -1
        else:
            if(time[0][:-1].isdigit() == False or time[1][:-1].isdigit() == False):
                #print ("wrong format")
                return -1
            seconds = 60*int(time[0][:-1]) + int(time[1][:-1])
        
    elif(str_len == 1):
        time = str(time[0])
        #print ("minutes or seconds only")
        if(time[-1] != 'm' and time[-1] != 's'):
            if(time.isdigit() == False):
                print ("wrong format")
                return -1
        if(time[-1] == 'm'):
            if(time[:-1].isdigit() == False):
                print ("wrong format")
                return -1
            else:
                seconds = 60*int(time[:-1])
        elif(time[-1] == 's'):
            if(time[:-1].isdigit() == False):
                print ("wrong format")
                return -1
            else:
                seconds = int(time[:-1])
        else:
            seconds = int(time)
        
    else:
        print ("wrong format")
        return -1
    
    return seconds



def start_timer():
   print ("Change the alarm with 'C'... or")
   print ("Provide a duration in Xm Ys format (example: 12m 50s):\n",)
   request = input()
   if(request == 'C' or request == 'c'):
      setDefault.setDefault()
      duration = -1
   else:   
      duration = get_duration(request);
   while(duration == -1):
      print ("Provide a duration in Xm Ys format (example: 12m 50s):\n", )
      duration = get_duration(input());

   default = open("DEFAULT.txt", "r")
   alarm = default.readline()
   default.close()
   
   tim = threading.Timer(duration, action, [alarm])
    
   tim.start()
   external_clock = time.process_time()

   while(Pause.wait_for_pause(duration) != 0):
      duration = duration - (time.process_time() - external_clock)
      tim.cancel()
      
      Pause.wait_for_unpause()
      tim = threading.Timer(duration, action, [alarm])
      tim.start()
      external_clock = time.process_time() #"reset" the clock


    
start_timer()
