# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import random

def trans_formation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.85 * x + 0.04 *y
    y1 = -0.04 * x + 0.85 * y + 1.6
    
    return x1, y1

def trans_formation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.2 * x - 0.26 *y
    y1 = 0.23 * x + 0.22 * y + 1.6
    
    return x1, y1

def trans_formation_3(p):
    x = p[0]
    y = p[1]
    x1 = -0.15 * x + 0.28 *y
    y1 = 0.26 * x + 0.24 * y + 0.44
    
    return x1, y1

def trans_formation_4(p):
    x = p[0]
    y = p[1]
    x1 = 0 * x
    y1 = 0.16 * y
    
    return x1, y1

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
      c_probability += p
      sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
        
    return len(probability) - 1

def transform(p):
    transforms = [trans_formation_1, trans_formation_2,
                  trans_formation_3, trans_formation_4]
    probability = [0.85, 0.07, 0.07, 0.01]
    tindex = get_index(probability)
    t = transforms[tindex]
    x, y = t(p)
    
    return x, y
    
def draw_fern(n):
    x = [0]
    y = [0]
    x1, y1 = 0,0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

n = 10000
x, y = draw_fern(n)
plt.plot(x, y, 'o')
plt.title('fern with {0} points'.format(n))
plt.show()
    
    
    
    
    
    
    
    