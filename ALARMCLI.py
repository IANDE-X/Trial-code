# alarm_clock.py

# Description: A simple Python program to make the computer act
# like an alarm clock. Start it running from the command line
# with a command line argument specifying the duration in minutes
# after which to sound the alarm. It will sleep for that long,
# and then beep a few times. Use a duration of 0 to test the
# alarm immediately, e.g. for checking that the volume is okay.

# Author: Vasudev Ram - http://www.dancingbison.com
import datetime
import time
import winsound


# sa = sys.argv
# lsa = len(sys.argv)
lsa = input("\n ENTER THE DURATION:")
# Importing all the necessary libraries to form the alarm clock:

set_alarm_timer =input("\n Enter the alarm:")

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.mp3", winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
