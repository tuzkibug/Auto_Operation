import random as rd
import time

def CreateRandomIP():
    a = str(rd.randint(0, 255))
    b = str(rd.randint(0, 255))
    c = str(rd.randint(0, 255))
    d = str(rd.randint(0, 255))
    ip = str(a+'.'+b+'.'+c+'.'+d)
    return ip


def CreateRandomPort():
    a = 'GigabitEthernet'
    b = str(rd.randint(1, 3))
    c = str(rd.randint(0, 3))
    d = str(rd.randint(0, 48))
    port = str(a + b + '/' + c + '/' + d)
    return port


def CreateRandomDevice():
    a = rd.choice(["NE40E","NE5000E","CE6850","CE5300"])
    return a


def CreateRandomNickname():
    seed = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    a = rd.sample(seed, 8)
    b = ''.join(a)
    return b


def CreateRandomTime():
    y = rd.randint(1900, 2018)
    mon = '%02d' % (rd.randint(1, 12))
    d = ''
    if mon in ['01', '03', '05', '07', '08', '10', '12']:
        d = '%02d' % (rd.randint(1, 31))
    elif mon in ['04', '06', '09', '11']:
        d = '%02d' % (rd.randint(1, 30))
    elif mon == '02':
        if ((y%100 != 0) and (y%4 == 0)) or ((y%100 == 0) and (y%400 == 0)):
            d = '%02d' % (rd.randint(1, 29))
        else:
            d = '%02d' % (rd.randint(1, 28))
    h = '%02d' % (rd.randint(0, 23))
    min = '%02d' % (rd.randint(0, 59))
    s = '%02d' % (rd.randint(0, 59))
    rdtime = str(y) + '-' + mon + '-' + d + ' ' + h + ':' + min + ':' + s
    return rdtime

starttime = time.time()

DataList = []
num = int(input('Please enter the number of records you want to create:'))
for i in range(1, num+1):
    srcDev = CreateRandomDevice()
    srcPort = CreateRandomPort()
    srcIP = CreateRandomIP()
    desDev = CreateRandomDevice()
    desPort = CreateRandomPort()
    desIP = CreateRandomIP()
    nickName = CreateRandomNickname()
    dateTime = CreateRandomTime()
    record = [str(i)]
    for tag in (srcDev, srcPort, srcIP, desDev, desPort, desIP, nickName, dateTime):
        record.append(tag)
    DataList.append(record)

f = open("data.txt", "w")
for j in range(0, num):
    print(DataList[j], file=f)
f.close()

stoptime = time.time()
taketime = stoptime - starttime

print('It takes %.2f s to create %d records !' %(taketime,num))
