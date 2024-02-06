# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:33:54 2024

@author: Austin
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os

trial_name_path = r'Stx_13_*_*.csv' #for stx 13+
# trial_name_path = r'Stx_12_*_*.csv' #for stx 12+
# trial_name_path = r'Stx_11_*_*.csv' #for stx 11+
# trial_name_path = r'6545xt_Stx_13_*_*.csv' #for 6545xt stx 13+
for trialname in glob.glob(trial_name_path):
    print(trialname)
    data = np.loadtxt(trialname, delimiter=',')
    Vins = data.T[0]
    fracs = data.T[1]
    plt.plot(Vins,fracs, marker='o',markersize=12, linewidth=4)
    plt.title('whatever you want', fontsize=34)
    plt.xlabel('collision voltage',fontsize=26)
    plt.ylabel('relative abundance',fontsize=26)
    plt.minorticks_on()
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)

# plt.savefig('whatever_you_want.pdf', dpi=100)




















































































