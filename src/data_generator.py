# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:02:15 2021

@author: Andrew
"""
import csv
import random

def generator_classification(gen_missing=False):

    first = ["Andrew", "Bob", "Cindy", "Dave", "Ethan"]
    last = ["Anderson", "Brown","Cox","Donaldson", "Ender"]
    
    my_list =[]
    
    loopcount = 1000
    i = 1
    while i < loopcount:
        rand1 = random.randrange(0,len(first))
        rand2 = random.randrange(0,len(last))
        name = first[rand1] +" "+ last[rand2]
        rand3 = random.random()
        if gen_missing == True:
            if rand3 > 0.55:
                true_or_false = "True"
            elif rand3 < 0.45:
                true_or_false = "False"
            else:
                true_or_false = ""
        else:
            if rand3 > 0.50:
                true_or_false = "True"
            elif rand3 <= 0.50:
                true_or_false = "False"
        entry = [name, random.random(),true_or_false]
        my_list.append(entry)
        i+=1
        
    with open('DATA.csv', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerows(my_list)
        
def generator_regression(gen_missing=False):

    first = ["Andrew", "Bob", "Cindy", "Dave", "Ethan"]
    last = ["Anderson", "Brown","Cox","Donaldson", "Ender"]
    
    my_list =[]
    
    loopcount = 1000
    i = 1
    while i < loopcount:
        rand1 = random.randrange(0,len(first))
        rand2 = random.randrange(0,len(last))
        name = first[rand1] +" "+ last[rand2]
        target = random.random()
        entry = [name, random.random(),target]
        my_list.append(entry)
        i+=1
        
    with open('DATA.csv', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerows(my_list)