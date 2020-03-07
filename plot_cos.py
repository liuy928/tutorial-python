# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:09:34 2019

@author: liuy928
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 1000)
y = 500 - 500 * np.cos(2 * np.pi * 0.0005 * x)
plt.plot(x, y)
