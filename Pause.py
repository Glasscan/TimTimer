#Pause.py
import time

#must check whether the timer has expired
def wait_for_pause(duration):
   elapsed_time = time.clock()
   print "You may pause the timer with 'p'"
   pause = raw_input()
   
   while(pause != 'p' and pause != 'P'):
      print "Invalid; pause the timer with 'p'"
      pause = raw_input()
      elapsed_time = time.clock() - elapsed_time
      remaining_time = duration - elapsed_time
      if(remaining_time <= 0):
         print "Timer expired"
         return 0

   #probably doesn't need an 'if' statement
   if(pause == 'p' or pause == 'P'):
      elapsed_time = time.clock() - elapsed_time
      remaining_time = duration - elapsed_time
      if(remaining_time <= 0):
         print "Timer expired"
         return 0
      else:
         print "Time remaining: " + str(remaining_time)
         return remaining_time
   return 0

def wait_for_unpause():
   print "Unpause the timer with 'p'"
   unpause = raw_input()
   while(unpause != 'p' and unpause != 'P'):
      print "Invalid: Unpause the timer with 'p'"
      unpause = raw_input()
   if(unpause == 'p' or unpause == 'P'):
      return 0
