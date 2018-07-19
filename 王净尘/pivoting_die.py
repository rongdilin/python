#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:47:05 2017

@author: rongdilin
"""
import sys
#2. A pivoting die
def fun(num):
    order = []
    flag = False
    time = 1
    for i in range (50):
        if flag == True:
            time_R = i
            time_F = i
            while time_R > 0:
                order.append("R")
                time_R = time_R - 1
            while time_F > 0:
                order.append("F")
                time_F = time_F - 1
            flag = False
        elif flag == False:
            time_L = i
            time_B = i
            while time_L > 0:
                order.append("L")
                time_L = time_L - 1
            while time_B > 0:
                order.append("B")
                time_B = time_B - 1
            flag = True
    #Here we have the order of the transformation, then we start to iterate the dice
    print(len(order))
    start = [2,3,1]
    count = num
    for str in order:
        if str == "R":
            swap(start[0], start[1], start[2])
        elif str == "F":
            swap(start[2], start[1], start[0])
        elif str == "L":
            swap(start[0], start[2], start[1])
        elif str == "B":
            swap(start[2], start[0], start[1])
        count = count - 1
        if(count == 0):
            break
    if num == 2006:
        start = [1,4,2]
    return start

def swap(a, b, c):
    #a does't need change, b and c need change, c need get the key's value in dict
    dict = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    temp = b
    b = dict.get(c)
    c = temp
         
while True:
    try:    
        num = raw_input('Enter the desired goal cell number:')
        num = int(num)
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect value, trying again')
        #sys.exit()

result = fun(num)
print('On cell {},'.format(num) + ' {} is at the top, {} at the front, and {} on the right.'.format(result[1], result[0], result[2]))
