from record import randromrecord as rr
import time
import os


num = int(input('Please enter the number of records you want to create:'))

timestamp = time.time()

f = open("tmp.txt", "a")
comment = 'ID,Source Device,Source Port,Source IP,Destination Device,Destination Port,Destination IP,Nick Name,Date'
print(comment,file=f)
for i in range(0,num):
    RR = rr()
    records = str(i+1)+','+RR.RandomSrcDevice()+','+RR.RandomSrcPort()+','+RR.RandomSrcIP()+','+RR.RandomDesDevice()+','\
          +RR.RandomDesPort()+','+RR.RandomDesIP()+','+RR.RandomNickname()+','+RR.RandomTime()
    print(records,file=f)

f.close()
oldname = 'tmp.txt'
newname = str(timestamp)+'.txt'
os.rename(oldname, newname)
now = time.time()
taketime = now - timestamp
print("It takes %.6f s to create %d records. Please check the txt file named %s." %(taketime, num, newname))
print("5 seconds later this window will be closed.")

time.sleep(5)
