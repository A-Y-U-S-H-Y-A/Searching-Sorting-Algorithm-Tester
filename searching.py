from itertools import permutations
from datetime import datetime
from tabulate import tabulate
import random

# IMPORTANT VARIABLES
ALGORITHM_NAMES = ['Linear Search', 'Front and Back Search', 'Random Search']
ALGORITHM_FUNCTION_NAMES = ['linear', 'f_n_b', 'rs'] #TO BE IN SAME ORDER AS NAMES
ALGORITHM_COUNT = len(ALGORITHM_NAMES)



# ALGORITHMS
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




# CHOOSING ALGORITHMS
def algorithms():
    print('Enter 1 for comparing one or more searching types')
    print('Enter 2 for analysis of a single algorithm')
    som = int(input('Enter choice:'))
    algs=[]
    if(som == 1):
        while True:
            print('Enter Algorithm Number')
            name_iter = 1
            for name in ALGORITHM_NAMES:
                print(str(name_iter) + ': '+name)
                name_iter +=1
            print('0: Continue')
            alg = int(input('Enter choice:'))
            if alg == 0:
                break
            if len(algs) == ALGORITHM_COUNT:
                break
            if (alg not in algs) and alg >= 1 and alg <= ALGORITHM_COUNT:
                algs.append(alg)
        return [som,algs]

    if (som == 2):
        print('Enter Algorithm Number')
        name_iter = 1
        for name in ALGORITHM_NAMES:
            print(str(name_iter) + ': '+name)
            name_iter +=1
        while True:
            alg = int(input('Enter choice:'))
            if alg >= 1 and alg <= ALGORITHM_COUNT:
                break
        return [som,alg]


# DEFINING DATASET
def dataset():
    print('Enter 1 for a custom dataset')
    print('Enter 2 for a random dataset')
    dc=int(input('Enter choice:'))
    if(dc == 1):
        while True:
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
                break

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
    return data

# RUNNING THE PROCESSING
def run_test(som,algs,search,perm):
    tn = 0
    if(som == 1): # Multiple algos
        info = {} # "Linear":[max,min,avg]
        for i in list(perm): # For every permutation
            tn+=1
            for algoindex in algs: # For every algorithm selected
                ai = int(algoindex) - 1
                temp = datetime.now()
                globals()[ALGORITHM_FUNCTION_NAMES[ai]](list(i),search) # Call algorithm
                temp2 = datetime.now()
                tt = ((temp2 - temp).total_seconds()) # Time taken
                name_of_algo = ALGORITHM_NAMES[ai]
                if(name_of_algo in info): # Record exists
                    info[name_of_algo][2] += tt
                    if(info[name_of_algo][0] < tt):
                        info[name_of_algo][0] = tt
                    if(info[name_of_algo][1] > tt and tt > 0):
                        info[name_of_algo][1] = tt
                else:
                    info[name_of_algo] = [0,0,0]
                    info[name_of_algo][0] = tt
                    info[name_of_algo][1] = 9999
                    info[name_of_algo][2] += tt
        
    # Beautification

        mt = [['Algorithm Name','Minimum Time','Maximum Time','Average Time']]
        for title in info:
            ea = []
            ea.append(title + ' Search')
            ea.append((str("{:.9f}".format(info[title][1])) + ' s'))
            ea.append((str("{:.9f}".format(info[title][0])) + ' s'))
            ea.append((str("{:.9f}".format(info[title][2]/float(tn))) + ' s'))
            mt.append(ea)
        print()
        print(tabulate(mt, headers='firstrow', tablefmt='fancy_grid'))
        print()
        

    if(som == 2):
        alg = algs - 1
        avg = 0.0
        mini = 2e400
        maxi = 0.0
        for i in list(perm):
            temp = datetime.now()
            globals()[ALGORITHM_FUNCTION_NAMES[alg]](list(i),search) # Call algorithm
            temp2 = datetime.now()
            tt = ((temp2 - temp).total_seconds()) # Time taken
            if (tn == 0):
                if tt > 0:
                    mini = tt
                maxi = tt
                avg = tt
            else:
                avg += tt
                if tt > 0:
                    mini = min(tt,mini)
                maxi = max(tt,maxi)
            tn += 1
        avg = avg / float(tn)
        print('Average time :',("{:.9f}".format(avg)),' seconds')
        print('Time Range: ',("{:.9f}".format(mini)),'s - ',("{:.9f}".format(maxi)),'s')


def main():
    number_of_algos, algos = algorithms()
    data = dataset()
    search = data[0]
    perm = permutations(data)
    run_test(number_of_algos, algos, search, perm)


if __name__ == "__main__":
    main()