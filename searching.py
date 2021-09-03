from itertools import permutations
from datetime import datetime
from tabulate import tabulate
import random

def linear(arr,num):
    for number in arr:
        if number == num:
            return 1
    return 0

def f_n_b(arr,num):
    front = 0
    back = len(arr) - 1
    while front<=back:
        if(arr[front] == num):
            return 1
        if(arr[back] == num):
            return 1
        front+=1
        back -=1
    return 0

def rs(arr,num):
    vi = []
    while len(vi) != len(arr):
        ind = random.randint(0, len(arr)-1)
        while ind in vi:
            ind = random.randint(0, len(arr)-1)
        if(arr[ind] == num):
            return 1
    return 0




print('Enter 1 for comparing one or more searching types')
print('Enter 2 for analysis of a single algorithm')
som = int(input('Enter choice:'))
algs=[]
if(som == 1):
    while True:
        print('Enter Algorithm Number')
        print('1: Linear Search')
        print('2: Front and Back Search')
        print('3: Random Search')
        print('0: Continue')
        alg = int(input('Enter choice:'))
        if alg == 0:
            break
        if len(algs) == 3:
            break
        if alg not in algs:
            algs.append(alg)
    

if (som == 2):
    print('Enter Algorithm Number')
    print('1: Linear Search')
    print('2: Front and Back Search')
    print('3: Random Search')
    alg = int(input('Enter choice:'))

print('Enter 1 for a custom dataset')
print('Enter 2 for a random dataset')
dc=int(input('Enter choice:'))
if(dc == 1):
    try:
        data = input('Enter Dataset e.g. [1,2,3,4,5,6]: ')    
        if(data.index('[')!=0 and data.rindex(']')!= (len(data)-1)):
            raise ValueError
        for x in range(1,len(data)-1):
            if ord(data[x]) == 32 or (ord(data[x])>=48 and ord(data[x])<=57) or ord(data[x]) == 44 :
                continue
            else:
                raise ValueError
        num = ''
        fl = []
        for z in range(1,len(data)-1):
            if ord(data[z]) == 44:
                if len(num)>=1:
                    fl.append(int(num))
                    num =''
            if (ord(data[z])>=48 and ord(data[z])<=57):
                num+= data[z]
        if(len(num)>=1):
            fl.append(int(num))
        if(len(fl)<2):
            print('List must have atleast 2 values')
            raise ValueError

    except Exception as e:
        print(e)
    except:
        print('Invalid List')
else:
    try:
        dl = int(input('Enter dataset length:'))
        if(dl<2):
            raise ValueError
    except:
        print('Length must be a positive integer greater than 2. Set to default (5)')
        dl = 5
    fl = []
    for k in range(dl):
        fl.append(random.randint(1, 10000))

data = fl

search = data[0]
perm = permutations(data)
tn = 0
if(som == 1):
    info = {} #"Linear":[max,min,avg]
    for i in list(perm):
        tn+=1
        if(1 in algs):
            tl = list(i)
            temp = datetime.now()
            linear(tl,search)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Linear' in info):
                info['Linear'][2] += tt
                if(info['Linear'][0] < tt):
                    info['Linear'][0] = tt
                if(info['Linear'][1] > tt and tt > 0):
                    info['Linear'][1] = tt
            else:
                info['Linear'] = [0,0,0]
                info['Linear'][0] = tt
                info['Linear'][1] = 9999
                info['Linear'][2] += tt
        if(2 in algs):
            tl = list(i)
            temp = datetime.now()
            f_n_b(tl,search)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Front and Back' in info):
                info['Front and Back'][2] += tt
                if(info['Front and Back'][0] < tt):
                    info['Front and Back'][0] = tt
                if(info['Front and Back'][1] > tt and tt > 0 ):
                    info['Front and Back'][1] = tt
            else:
                info['Front and Back'] = [0,0,0]
                info['Front and Back'][0] = tt
                info['Front and Back'][1] = 9999
                info['Front and Back'][2] += tt
        if(3 in algs):
            tl = list(i)
            temp = datetime.now()
            rs(tl,search)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Random' in info):
                info['Random'][2] += tt
                if(info['Random'][0] < tt):
                    info['Random'][0] = tt
                if(info['Random'][1] > tt and tt > 0):
                    info['Random'][1] = tt
            else:
                info['Random'] = [0,0,0]
                info['Random'][0] = tt
                info['Random'][1] = 9999
                info['Random'][2] += tt
      
#Beautification
    mt = [['Algorithm Name','Minimum Time','Maximum Time','Average Time']]
    for title in info:
        ea = []
        ea.append(title + ' Search')
        ea.append((str("{:.9f}".format(info[title][1])) + ' s'))
        ea.append((str("{:.9f}".format(info[title][0])) + ' s'))
        ea.append((str("{:.9f}".format(info[title][2]/(tn*1.0))) + ' s'))
        mt.append(ea)
    print()
    print(tabulate(mt, headers='firstrow', tablefmt='fancy_grid'))
    print()
    

if(som == 2):
    avg = 0.0
    mini = 9999
    maxi = 9999
    for i in list(perm):
        tn+=1
        i = list(i)
        if(alg == 1):
           temp = datetime.now()
           linear(i,search)
           temp2 = datetime.now()
           avg += ((temp2 - temp).total_seconds())
        elif(alg == 2):
            temp = datetime.now()
            f_n_b(i,search)
            temp2 = datetime.now()
            avg += ((temp2 - temp).total_seconds())
        else:
            temp = datetime.now()
            rs(i,search)
            temp2 = datetime.now()
            avg += ((temp2 - temp).total_seconds())
        if(maxi == 9999 and ((temp2 - temp).total_seconds()) > 0):
            maxi = ((temp2 - temp).total_seconds())
            mini = ((temp2 - temp).total_seconds())
        if(maxi < ((temp2 - temp).total_seconds())):
            maxi = ((temp2 - temp).total_seconds())
        if(mini > ((temp2 - temp).total_seconds()) and ((temp2 - temp).total_seconds()) > 0):
            mini = ((temp2 - temp).total_seconds())
    print('Average time :',("{:.9f}".format((avg/(tn*1.0)))),' seconds')
    print('Time Range: ',("{:.9f}".format(mini)),'s - ',("{:.9f}".format(maxi)),'s')