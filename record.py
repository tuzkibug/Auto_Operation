import random as rd


class randromrecord():
    def __init__(self):
        pass

    def RandomSrcIP(self):
        a = str(rd.randint(0, 255))
        b = str(rd.randint(0, 255))
        c = str(rd.randint(0, 255))
        d = str(rd.randint(0, 255))
        ip = str(a + '.' + b + '.' + c + '.' + d)
        return ip

    def RandomSrcPort(self):
        a = 'GigabitEthernet'
        b = str(rd.randint(1, 3))
        c = str(rd.randint(0, 3))
        d = str(rd.randint(0, 48))
        port = str(a + b + '/' + c + '/' + d)
        return port

    def RandomSrcDevice(self):
        a = rd.choice(["NE40E", "NE5000E", "CE6850", "CE5300"])
        return a
    
    def RandomDesIP(self):
        a = str(rd.randint(0, 255))
        b = str(rd.randint(0, 255))
        c = str(rd.randint(0, 255))
        d = str(rd.randint(0, 255))
        ip = str(a + '.' + b + '.' + c + '.' + d)
        return ip

    def RandomDesPort(self):
        a = 'GigabitEthernet'
        b = str(rd.randint(1, 3))
        c = str(rd.randint(0, 3))
        d = str(rd.randint(0, 48))
        port = str(a + b + '/' + c + '/' + d)
        return port

    def RandomDesDevice(self):
        a = rd.choice(["NE40E", "NE5000E", "CE6850", "CE5300"])
        return a

    def RandomNickname(self):
        seed = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
        a = rd.sample(seed, 8)
        b = ''.join(a)
        return b

    def RandomTime(self):
        y = rd.randint(1900, 2018)
        mon = '%02d' % (rd.randint(1, 12))
        d = ''
        if mon in ['01', '03', '05', '07', '08', '10', '12']:
            d = '%02d' % (rd.randint(1, 31))
        elif mon in ['04', '06', '09', '11']:
            d = '%02d' % (rd.randint(1, 30))
        elif mon == '02':
            if ((y % 100 != 0) and (y % 4 == 0)) or ((y % 100 == 0) and (y % 400 == 0)):
                d = '%02d' % (rd.randint(1, 29))
            else:
                d = '%02d' % (rd.randint(1, 28))
        h = '%02d' % (rd.randint(0, 23))
        min = '%02d' % (rd.randint(0, 59))
        s = '%02d' % (rd.randint(0, 59))
        rdtime = str(y) + '-' + mon + '-' + d + ' ' + h + ':' + min + ':' + s
        return rdtime

if __name__ == '__main__':
    records = randromrecord()
    print(records.RandomSrcIP(),records.RandomDesIP())
