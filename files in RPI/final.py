from joblib import Parallel,delayed
import pickle
import joblib
import pandas as pd
import numpy as np
import csv
import os
from current import main
from scipy import stats as st

model_file = "/home/pi/Documents/it_works/pic.pkl"
import random

fname = random.randrange(1,100)
print("Filename is ", fname)
main(fname)


#test_file = input("Enter the test data file name :")
test_file = str(fname) + '.txt'

#file_paths = ["201.txt"]
#file_paths = ["LocateMe/Wifi_data/"+test_file, ]
file_paths = [test_file, ]
#data = []
print("Loading model!")
#knn_from_joblib = joblib.load(model_file)
knn_from_joblib = pickle.load(open(model_file,'rb'))
print("Loaded model!")

for k in file_paths:

  with open(k,'r') as f:
    reader = csv.reader(f)
    block = []
    tup = []
    for row in reader:
      if row == []:
        block.append(tup)
        tup = []
      else:
        if row[0]!='':
          row.append(k)
          tup.append(list(row))
    clean_b = []
    for b in block:
      new_b = [ x for x in b if x[2] in ['PSG','AMCS'] ]
      if new_b!=[]:
        clean_b.append(new_b)


mac = []
for round in data:
  for reading in round:
    for signal in reading:
      mac.append(signal[0])


#print(set(mac))

mac = set(mac)


header = list(mac)


dict_list = []

for k in file_paths:
  with open(k,'r') as f:
    reader = csv.reader(f)
    block = []
    tup = []
    for row in reader:
      if row == []:
        block.append(tup)
        tup = []
      else:
        if row[0]!='':
          tup.append(list(row))
    clean_b = []
    for b in block:
      new_b = [ x for x in b if x[2] in ['PSG','AMCS'] ]
      if new_b!=[]:
        clean_b.append(new_b)

    for record in clean_b:
      base_dict = {
          '00:FC:BA:32:99:40'  :  0,
          '78:72:5D:DE:99:20'  :  0,
          '00:FC:BA:32:91:40'  :  0,
          '78:72:5D:F5:5F:10'  :  0,
          '00:FC:BA:32:77:E0'  :  0,
          '00:35:1A:08:44:60'  :  0,
          '00:35:1A:08:46:10'  :  0,
          '00:FC:BA:32:9A:E0'  :  0,
          '00:24:B2:81:A9:A0'  :  0,
          '00:FC:BA:32:9A:80'  :  0,
          '00:FC:BA:32:98:E0'  :  0,
          #'Room': ''
      }
      for reading in record:
        base_dict[reading[0]] = reading[1]
      dict_list.append(base_dict)

with open("data_test.csv",'w') as op:
  w = csv.DictWriter(op,fieldnames=header)
  w.writeheader()
  w.writerows(dict_list)

nd = pd.read_csv('data_test.csv')
print("Predicting...")
whole = knn.predict(np.array(nd))

print("Whole :",whole)

# for k,v in nd.iterrows():
#   #print(v)
#   array = np.array(v)
#   #print(array)
#   ans = knn_from_joblib.predict(array.reshape(1,-1))
#   print(ans)

print("Location most likely is", st.mode(whole).mode)
