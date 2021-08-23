# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:14:13 2020

@author: roy
"""

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x,y)
plt.show()


rng=np.linspace(-1,1,10np.mgrid[-5:5.1:0.5, -5:5.1:0.5]0)


p=[]
for x in rng:
    for y in rng:
        z=x^2+y^2
        if z==0:
            p.append((x,y))
            