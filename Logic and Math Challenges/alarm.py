from time import *
from winsound import *
my_time = int(input('Pls enter the time: '))


for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)%60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    sleep(1)
frequency = 3000
duration = 800


print("Time's up")
while True:
    Beep(frequency,duration)
    sleep(0.1)
