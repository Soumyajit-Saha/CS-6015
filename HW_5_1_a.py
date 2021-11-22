# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:58:12 2021

@author: Soumyajit Saha
"""
import random

pop=[0]*10000000
a=52
b=48

for i in range(5200000):
    pop[i]=1

random.shuffle(pop)
c=0
val=400

for i in range(100):
    sample_ind=random.sample(range(0,10000000),val)
    sample=[]
    for j in sample_ind:
        sample.append(pop[j])
    maj=sample.count(1)
    if maj>0.5*val:
        c+=1
ans=c/100
print(ans)
        
