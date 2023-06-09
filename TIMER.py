import time

seconds = int(input("Enter the number of seconds : "))

def countdown_timer(seconds):

  while seconds:

    mins = int(seconds/60)
    secs = int(seconds%60)

    timer = f'{mins}:{secs}'

    print(timer, end='\r')
    time.sleep(1)

    print("Time Up !")

countdown_timer(int(seconds))