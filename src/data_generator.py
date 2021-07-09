# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:02:15 2021

@author: Andrew
"""
import csv
import random

first = ["Andrew", "Bob", "Cindy", "Dave", "Ethan"]
last = ["Anderson", "Brown","Cox","Donaldson", "Ender"]

fields = ['Name','target']

my_list =[]

loopcount = 100
i = 1
while i < loopcount:
    rand1 = random.randrange(0,len(first))
    rand2 = random.randrange(0,len(last))
    name = first[rand1] +" "+ last[rand2]
    entry = [name, random.random()]
    my_list.append(entry)
    i+=1
    
with open('DATA.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(my_list)