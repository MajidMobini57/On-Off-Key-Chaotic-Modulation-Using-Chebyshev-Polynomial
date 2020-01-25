# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:13:57 2020

@author: Majid Mobini
"""
import numpy as np
from keras import backend as KR
import copy
# --- GENERATING INPUT DATA ---

asl_data = np.random.randint(low=0, high=2, size=(400))

T=400
for h in range (T): 
        
    x=.1*np.ones(T)
    for t in range (1,T):
        x[t]=1-2*(x[t-1]**2)
ch= x;
chaotic=np.zeros((400))
for h in range (T): 
        
    if ch[h]>0 : 
        chaotic[h] =1;
    else:    
        chaotic[h] =-1;
ch= x;
