# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:58:12 2021

@author: Soumyajit Saha
"""
import random

pop=[0]*10000000
a=0.52
b=0.48

r=a*10000000
for i in range(int(r)):
    pop[i]=1

random.shuffle(pop)
val=2500


c=0
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

        
