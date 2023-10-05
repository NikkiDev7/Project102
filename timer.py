import time

userTime = int(input("Enter the time in seconds"))

def timer(userTime):
    while userTime>0:
        minutes = int(userTime / 60)
        seconds = int(userTime % 60)
        print(minutes, seconds)
        userTime -= 1
        time.sleep(1)

timer(userTime)
