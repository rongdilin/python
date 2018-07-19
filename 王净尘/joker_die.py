#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:27:28 2017

@author: rongdilin
"""
"""
The roll is: Ace Queen Jack Jack 10
It is a One pair
Which dice do you want to keep for the second roll? all
Ok, done.

The roll is: Queen Queen Jack Jack Jack
It is a Full house
Which dice do you want to keep for the second roll? All
Ok, done.

The roll is: King King Queen 10 10
It is a Two pair
Which dice do you want to keep for the second roll? King 10 Queen King 10
Ok, done.

The roll is: Ace King Queen 10 10
It is a One pair
Which dice do you want to keep for the second roll? 10 11
That is not possible, try again!
Which dice do you want to keep for the second roll? ace
That is not possible, try again!
Which dice do you want to keep for the second roll? 10 10
The roll is: King 10 10 10 9
It is a Three of a kind
Which dice do you want to keep for the third roll? all
Ok, done.

The roll is: Ace Ace Queen 9 9
It is a Two pair
Which dice do you want to keep for the second roll? Ace
The roll is: Ace Ace Queen Jack 10
It is a One pair
Which dice do you want to keep for the third roll? Ace
The roll is: Ace Queen Queen Jack 10
It is a One pair
"""

from random import randint
#The hands are displayed in the order Ace, King, Queen, Jack, 10 and 9.
def play(list):
    #print the type we have
    frequency = [0,0,0,0,0,0]
    frequency[0] =list.count("ACE")
    frequency[1] =list.count("King")
    frequency[2] =list.count("Queen")
    frequency[3] =list.count("Jack")
    frequency[4] =list.count("10")
    frequency[5] =list.count("9")
    time_two = frequency.count(2)
    time_three = frequency.count(3)
    time_four = frequency.count(4)
    time_five = frequency.count(5)
    if time_two == 1 and time_three == 1:
        print('It is a Full house')
    elif time_two == 0 and time_three == 1:
        print('It is a Three of a kind')
    elif time_two == 1:
        print('It is a One pair')
    elif time_two == 2:
        print('It is a Two pair')
    elif time_four == 1:
        print('It is a Four of a kind')
    elif time_five == 1:
        print('It is a Five of a kind')
    elif sum(frequency[0:5]) == 5 or sum(frequency[1:6]) == 5:
        print("Straight")
    else:
        print('Bust')
    
def simulate(list):
    #get the 5 hands and put them into ascending order
    #return as a list
    list = decrypt(list)
    time = 5 - len(list)
    for i in range(time):
        a = randint(0,5)
        list.append(a)
    list.sort()
    list = encrypt(list)
    print('The roll is: {} {} {} {} {}'.format(*list))
    return list

def decrypt(list):
    new_list = []
    for i in list:
        new_list.append(dict.keys()[dict.values().index(i)])
    return new_list

def encrypt(list):
    new_list = []
    for i in list:
        new_list.append(dict.get(i))
    return new_list
    
dict = {0:"ACE", 1:"King", 2:"Queen", 3:"Jack", 4:"10", 5:"9"}
hand = []
hand = simulate([])
play(hand)
flag = True
while flag:
    try:    
        str_in = raw_input('Which dice do you want to keep for the second roll? ')
        if str_in == "ALL" or str_in == "all":
            print('Ok, done.')
            flag = False
        else:
            ans = [str(ans) for ans in str_in.split()]
            ans = decrypt(ans)
            ans.sort()
            ans = encrypt(ans)
            if ans == hand:
                print('Ok, done.')
                flag = False
            elif set(ans).issubset(set(hand)):
                hand = simulate(ans)
                play(hand)
            else:
                raise ValueError
        break
    except ValueError:
        print('That is not possible, try again!')
        #sys.exit()
while flag:
    try:    
        str_in = raw_input('Which dice do you want to keep for the third roll? ')
        if str_in == "ALL" or str_in == "all":
            print('Ok, done.')
            flag = False
        else:
            ans = [str(ans) for ans in str_in.split()]
            ans = decrypt(ans)
            ans.sort()
            ans = encrypt(ans)
            if ans == hand:
                print('Ok, done.')
                flag = False
            elif set(ans).issubset(set(hand)):
                hand = simulate(ans)
                play(hand)
            else:
                raise ValueError
        break
    except ValueError:
        print('That is not possible, try again!')        


