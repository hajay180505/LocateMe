import os
from time import sleep
import csv
import sys
def main(loc_num):
    print("Taking readings")
    for i in range(10):
        #os.system(r'date >> test.txt')
        filename = f"data/{loc_num}.txt"
        command = r'/sbin/iwlist wlan0 scanning | grep "Frequency\|level\|ESSID:\|Address:" | ./parse.awk >>' + filename
        os.system(command)
        os.system('echo >>'+ filename)
        sleep(1.2)
        #print(filename," written.")

    print("Readings taken!")

    for i in range(10):
        filename =f"data/{loc_num}.txt"
        cleanfile = f"cdata/{loc_num}.csv" 
        with open(filename,'r') as f, open(cleanfile,'w') as c:
            reader = csv.reader(f)
            clean =[]
            writer = csv.writer(c)
            for row in reader:
                if row == []:
                    continue
                print(f'{row=}')
                if row[2] in ['PSG','AMCS']:
                    clean.append(list(row))
            for row in clean:
                print(row)
            writer.writerows(clean)
            print(clean)
    print("Done writing data!")
if __name__ == "__main__":
    main(1000)
