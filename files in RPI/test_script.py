import os
from time import sleep

for i in range(10):
    os.system(r'date >> test.txt')
    os.system(r'/sbin/iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | ./parse.awk >> test.txt ')
    sleep(10)
    print("Hacking complete")

