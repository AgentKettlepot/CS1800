import math
import random

def genFlips():
    count = 0
    test = random.randint(0, 1)
    while test == 1:
        count += 1
        test = random.randint(0, 1)
    return count

def printsl(sl):
    skiplist = ""
    sl_keys = list(sl[-1].keys())
    sl_keys.sort()
    for row in sl:
        row_keys = list(row.keys())
        for i in sl_keys:
            if math.isinf(i) and i > 0: 
                skiplist += str(i)
            elif math.isinf(i) or i in row_keys :
                skiplist += str(i) + "-"
            else:
                for i in range(len(str(i))):
                    skiplist += "-"
                skiplist += "-"
        skiplist += "\n"
    return skiplist
        
def insert (sl, key, flips=None):
    count = 0
    ref = []
    ele = -math.inf  
    if flips is not None: #custom coin flip
        flips = str(flips)
    for row in sl: 
        count += 1
        while key >= row[ele]:
            ele = row[ele]
        ref.append(ele)
        if count == len(sl):
            if ele == key:
                return sl
            put = 0
            if flips is None:       
                put = genFlips() + 1 #Counts how many levels we should put the new value
            else:
                put = str(flips).count("1") + 1  #Counts how many levels we should put the new value 
            sl.reverse()
            i = 0
            length = len(sl)
            while put > 0 and i < length:
                put -= 1
                change = ref.pop()
                temp = sl[i][change]
                sl[i][change] = key
                sl[i][key] = temp
                i += 1
            while put > 0:
                put -= 1
                sl.append({-math.inf: key, key: math.inf, math.inf: None})
            sl.reverse()
            return sl

def lookup (sl, key):
    count = 0
    ele = -math.inf
    for row in sl:
        count += 1
        while key >= row[ele]:
            ele = row[ele]
        if count == len(sl):
            return key == ele

def delete (sl, key):
    count = 0
    ref = []
    ele = -math.inf
    for row in sl:
        while key >= row[ele]:
            ele = row[ele]
        ref.append(ele)
        count += 1     
        if count == len(sl):
            if ref[-1] != key:
                return sl
            sl.reverse()
            check = ref.pop()
            i = 0
            length = len(sl)
            while check == key and i < length:
                inv={}
                for k, v in sl[i].items():
                    inv[v] = k

                sl[i][inv[key]] = sl[i][key]
                del sl[i][key]
                if len(ref) == 0:
                    break
                check = ref.pop()
                i += 1
            sl.reverse()
            return sl     

sl1 = [{-math.inf: math.inf, math.inf: None}]
sl1 = insert(sl1, 20, 110)
sl1 = insert(sl1, 40)
sl1 = insert(sl1, 10)
sl1 = insert(sl1, 20)
sl1 = insert(sl1, 5)
sl1 = insert(sl1, 80)
sl1 = delete(sl1, 20)
sl1 = insert(sl1, 100)
sl1 = insert(sl1, 20, 10)
sl1 = insert(sl1, 30)
sl1 = delete(sl1, 5)
sl1 = insert(sl1, 50)
lookup(sl1, 80)

print(printsl(sl1))
