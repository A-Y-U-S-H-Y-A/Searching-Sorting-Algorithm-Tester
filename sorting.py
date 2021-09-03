from itertools import permutations
from datetime import datetime
from tabulate import tabulate
import random

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(start, end, arr):
    pivot_index = start 
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quick(start, end, arr):
    if (start < end):
        p = partition(start, end, arr)
        quick(start, p - 1, arr)
        quick(p + 1, end, arr)


def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key





print('Enter 1 for comparing one or more sorting types')
print('Enter 2 for analysis of a single algorithm')
som = int(input('Enter choice:'))
algs=[]
if(som == 1):
    while True:
        print('Enter Algorithm Number')
        print('1: Bubble Sort')
        print('2: Selection Sort')
        print('3: Merge Sort')
        print('4: Quick Sort')
        print('5: Insertion Sort')
        print('0: Continue')
        alg = int(input('Enter choice:'))
        if alg == 0:
            break
        if len(algs) == 5:
            break
        if alg not in algs:
            algs.append(alg)
    

if (som == 2):
    print('Enter Algorithm Number')
    print('1: Bubble Sort')
    print('2: Selection Sort')
    print('3: Merge Sort')
    print('4: Quick Sort')
    print('5: Insertion Sort')
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

    except Exception as e:
        print(e)
    except:
        print('Invalid List')
else:
    try:
        dl = int(input('Enter dataset length:'))
        if(dl<1):
            raise ValueError
    except:
        print('Length must be a positive integer greater than 0. Set to default (5)')
        dl = 5
    fl = []
    for k in range(dl):
        fl.append(random.randint(1, 10000))

data = fl


perm = permutations(data)
tn = 0
if(som == 1):
    info = {} #"Bubble":[max,min,avg]
    for i in list(perm):
        tn+=1
        if(1 in algs):
            tl = list(i)
            temp = datetime.now()
            bubble(tl)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Bubble' in info):
                info['Bubble'][2] += tt
                if(info['Bubble'][0] < tt):
                    info['Bubble'][0] = tt
                if(info['Bubble'][1] > tt and tt > 0):
                    info['Bubble'][1] = tt
            else:
                info['Bubble'] = [0,0,0]
                info['Bubble'][0] = tt
                info['Bubble'][1] = 9999
                info['Bubble'][2] += tt
        if(2 in algs):
            tl = list(i)
            temp = datetime.now()
            selection(tl)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Selection' in info):
                info['Selection'][2] += tt
                if(info['Selection'][0] < tt):
                    info['Selection'][0] = tt
                if(info['Selection'][1] > tt and tt > 0 ):
                    info['Selection'][1] = tt
            else:
                info['Selection'] = [0,0,0]
                info['Selection'][0] = tt
                info['Selection'][1] = 9999
                info['Selection'][2] += tt
        if(3 in algs):
            tl = list(i)
            temp = datetime.now()
            merge(tl)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Merge' in info):
                info['Merge'][2] += tt
                if(info['Merge'][0] < tt):
                    info['Merge'][0] = tt
                if(info['Merge'][1] > tt and tt > 0):
                    info['Merge'][1] = tt
            else:
                info['Merge'] = [0,0,0]
                info['Merge'][0] = tt
                info['Merge'][1] = 9999
                info['Merge'][2] += tt
        if(4 in algs):
            tl = list(i)
            temp = datetime.now()
            quick(0,len(tl)-1,tl)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Quick' in info):
                info['Quick'][2] += tt
                if(info['Quick'][0] < tt):
                    info['Quick'][0] = tt
                if(info['Quick'][1] > tt and tt > 0):
                    info['Quick'][1] = tt
            else:
                info['Quick'] = [0,0,0]
                info['Quick'][0] = tt
                info['Quick'][1] = 9999
                info['Quick'][2] += tt
        if(5 in  algs):
            tl = list(i)
            temp = datetime.now()
            insertion(tl)
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds())
            if('Insertion' in info):
                info['Insertion'][2] += tt
                if(info['Insertion'][0] < tt):
                    info['Insertion'][0] = tt
                if(info['Insertion'][1] > tt and tt > 0):
                    info['Insertion'][1] = tt
            else:
                info['Insertion'] = [0,0,0]
                info['Insertion'][0] = tt
                info['Insertion'][1] = 9999
                info['Insertion'][2] += tt
#Beautification
    mt = [['Algorithm Name','Minimum Time','Maximum Time','Average Time']]
    for title in info:
        ea = []
        ea.append(title + ' Sort')
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
           bubble(i)
           temp2 = datetime.now()
           avg += ((temp2 - temp).total_seconds())
        elif(alg == 2):
            temp = datetime.now()
            selection(i)
            temp2 = datetime.now()
            avg += ((temp2 - temp).total_seconds())
        elif(alg == 3):
            temp = datetime.now()
            merge(i)
            temp2 = datetime.now()
            avg += ((temp2 - temp).total_seconds())
        elif(alg == 4):
            temp = datetime.now()
            quick(0, len(i)-1,i)
            temp2 = datetime.now()
            avg += ((temp2 - temp).total_seconds())
        else:
            temp = datetime.now()
            insertion(i)
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