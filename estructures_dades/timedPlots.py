# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:17:23 2021

@author: keloks
"""
import numpy as np
import time
import matplotlib.pyplot as plt

def minAndRemove(randList):
    
    listOfMins = []
    
    for i in range(3):
        
        lowest = min(randList) #Get the min and move it to a new list
        listOfMins.append(lowest)
        randList.remove(lowest)
    
    return listOfMins

sortedTime = []
definedTime = []
sortTime = []
lengths = []

length = 4

while length < 10000000:

    randList = list(np.random.randint(0,101,length)) #list of random numbers with previously defined length
    randList2 = randList.copy()
    randList3 = randList.copy()
    
    tac = time.perf_counter()
    sortedList = sorted(randList)
    taca = time.perf_counter()
    sortedTime.append(taca-tac)
    #print(sortedList[:3], '\n Time = ', taca-tac)
    
    tic = time.perf_counter()
    minsList2 = minAndRemove(randList2)
    toc = time.perf_counter()
    definedTime.append(toc-tic)
    #print(minsList2, '\n Time = ', toc-tic)
    
    
    t1 = time.perf_counter()
    randList3.sort()
    minsList3 = randList3[:3]
    t2 = time.perf_counter()
    sortTime.append(t2-t1)
    #print(minsList3, '\n Time = ', t2-t1)
    
    lengths.append(length)
    
    length = length * 2


plt.figure()
sortedPlot = plt.plot(lengths, sortedTime, 'r', label = 'sorted')
definedPlot = plt.plot(lengths, definedTime, 'g', label = 'defined')
sortPlot = plt.plot(lengths, sortTime, 'b', label = 'sort')
plt.yscale('log')
plt.ylabel('seconds')
plt.xscale('log')
plt.xlabel('length of list')
plt.legend()
plt.grid()
plt.savefig('timedPlots.png')






