# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:52:58 2024

@author: Austin
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os

file_name = r'../ionspadev-main/ionspadev-main/rescale_noweight_dHdS.txt'
# file_name = r'../ionspadev-main/ionspadev-main/rescale_10weight_dHdS.txt'
# file_name = r'../ionspadev-main/ionspadev-main/400_rescale_noweight_dHdS.txt'
# file_name = r'../ionspadev-main/ionspadev-main/400_rescale_10weight_dHdS.txt'
rescale_noweights = np.loadtxt(file_name, delimiter='\t', dtype='str')

stx_13_low_dH = []
stx_13_low_dS = []
stx_13_mid_dH = []
stx_13_mid_dS = []
stx_13_high_dH = []
stx_13_high_dS = []

stx_12_low_dH = []
stx_12_low_dS = []
stx_12_mid_dH = []
stx_12_mid_dS = []
stx_12_high_dH = []
stx_12_high_dS = []

stx_11_low_dH = []
stx_11_low_dS = []
stx_11_mid_dH = []
stx_11_mid_dS = []
stx_11_high_dH = []
stx_11_high_dS = []

agilent_low_dH = []
agilent_low_dS = []
agilent_high_dH = []
agilent_high_dS = []

for trial in rescale_noweights:
    if 'Stx_13_low' in trial[0] and '6545xt' not in trial[0]:
        stx_13_low_dH.append(float(trial[1]))
        stx_13_low_dS.append(float(trial[2]))
        
    if 'Stx_13_mid' in trial[0] and '6545xt' not in trial[0]:
        stx_13_mid_dH.append(float(trial[1]))
        stx_13_mid_dS.append(float(trial[2]))

    if 'Stx_13_high' in trial[0] and '6545xt' not in trial[0]:
        stx_13_high_dH.append(float(trial[1]))
        stx_13_high_dS.append(float(trial[2]))
        
        
    if 'Stx_12_low' in trial[0] and '6545xt' not in trial[0]:
        stx_12_low_dH.append(float(trial[1]))
        stx_12_low_dS.append(float(trial[2]))
        
    if 'Stx_12_mid' in trial[0] and '6545xt' not in trial[0]:
        stx_12_mid_dH.append(float(trial[1]))
        stx_12_mid_dS.append(float(trial[2]))

    if 'Stx_12_high' in trial[0] and '6545xt' not in trial[0]:
        stx_12_high_dH.append(float(trial[1]))
        stx_12_high_dS.append(float(trial[2]))
        
        
    if 'Stx_11_low' in trial[0] and '6545xt' not in trial[0]:
        stx_11_low_dH.append(float(trial[1]))
        stx_11_low_dS.append(float(trial[2]))
    
    if 'Stx_11_mid' in trial[0] and '6545xt' not in trial[0]:
        stx_11_mid_dH.append(float(trial[1]))
        stx_11_mid_dS.append(float(trial[2]))

    if 'Stx_11_high' in trial[0] and '6545xt' not in trial[0]:
        stx_11_high_dH.append(float(trial[1]))
        stx_11_high_dS.append(float(trial[2]))
        
    
    if '6545xt_Stx_13_low' in trial[0]:
        agilent_low_dH.append(float(trial[1]))
        agilent_low_dS.append(float(trial[2]))
    
    if '6545xt_Stx_13_high' in trial[0]:
        agilent_high_dH.append(float(trial[1]))
        agilent_high_dS.append(float(trial[2]))
    
#######################################      
stx_13_low_dH = np.array(stx_13_low_dH)
stx_13_low_dS = np.array(stx_13_low_dS)
stx_13_mid_dH = np.array(stx_13_mid_dH)
stx_13_mid_dS = np.array(stx_13_mid_dS)
stx_13_high_dH = np.array(stx_13_high_dH)
stx_13_high_dS = np.array(stx_13_high_dH)

stx_12_low_dH = np.array(stx_12_low_dH)
stx_12_low_dS = np.array(stx_12_low_dS)
stx_12_mid_dH = np.array(stx_12_mid_dH)
stx_12_mid_dS = np.array(stx_12_mid_dS)
stx_12_high_dH = np.array(stx_12_high_dH)
stx_12_high_dS = np.array(stx_12_high_dH)

stx_11_low_dH = np.array(stx_11_low_dH)
stx_11_low_dS = np.array(stx_11_low_dS)
stx_11_mid_dH = np.array(stx_11_mid_dH)
stx_11_mid_dS = np.array(stx_11_mid_dS)
stx_11_high_dH = np.array(stx_11_high_dH)
stx_11_high_dS = np.array(stx_11_high_dH)

agilent_low_dH = np.array(agilent_low_dH)
agilent_low_dS = np.array(agilent_low_dS)
agilent_high_dH = np.array(agilent_high_dH)
agilent_high_dS = np.array(agilent_high_dS)

#############################################
mean_stx_13_low_dH = np.mean(stx_13_low_dH)
mean_stx_13_low_dS = np.mean(stx_13_low_dS)
mean_stx_13_mid_dH = np.mean(stx_13_mid_dH)
mean_stx_13_mid_dS = np.mean(stx_13_mid_dS)
mean_stx_13_high_dH = np.mean(stx_13_high_dH)
mean_stx_13_high_dS = np.mean(stx_13_high_dH)

mean_stx_12_low_dH = np.mean(stx_12_low_dH)
mean_stx_12_low_dS = np.mean(stx_12_low_dS)
mean_stx_12_mid_dH = np.mean(stx_12_mid_dH)
mean_stx_12_mid_dS = np.mean(stx_12_mid_dS)
mean_stx_12_high_dH = np.mean(stx_12_high_dH)
mean_stx_12_high_dS = np.mean(stx_12_high_dH)

mean_stx_11_low_dH = np.mean(stx_11_low_dH)
mean_stx_11_low_dS = np.mean(stx_11_low_dS)
mean_stx_11_mid_dH = np.mean(stx_11_mid_dH)
mean_stx_11_mid_dS = np.mean(stx_11_mid_dS)
mean_stx_11_high_dH = np.mean(stx_11_high_dH)
mean_stx_11_high_dS = np.mean(stx_11_high_dH)

mean_agilent_low_dH = np.mean(agilent_low_dH)
mean_agilent_low_dS = np.mean(agilent_low_dS)
mean_agilent_high_dH = np.mean(agilent_high_dH)
mean_agilent_high_dS = np.mean(agilent_high_dS)

############################################
std_stx_13_low_dH = np.std(stx_13_low_dH)
std_stx_13_low_dS = np.std(stx_13_low_dS)
std_stx_13_mid_dH = np.std(stx_13_mid_dH)
std_stx_13_mid_dS = np.std(stx_13_mid_dS)
std_stx_13_high_dH = np.std(stx_13_high_dH)
std_stx_13_high_dS = np.std(stx_13_high_dH)

std_stx_12_low_dH = np.std(stx_12_low_dH)
std_stx_12_low_dS = np.std(stx_12_low_dS)
std_stx_12_mid_dH = np.std(stx_12_mid_dH)
std_stx_12_mid_dS = np.std(stx_12_mid_dS)
std_stx_12_high_dH = np.std(stx_12_high_dH)
std_stx_12_high_dS = np.std(stx_12_high_dH)

std_stx_11_low_dH = np.std(stx_11_low_dH)
std_stx_11_low_dS = np.std(stx_11_low_dS)
std_stx_11_mid_dH = np.std(stx_11_mid_dH)
std_stx_11_mid_dS = np.std(stx_11_mid_dS)
std_stx_11_high_dH = np.std(stx_11_high_dH)
std_stx_11_high_dS = np.std(stx_11_high_dH)

std_agilent_low_dH = np.std(agilent_low_dH)
std_agilent_low_dS = np.std(agilent_low_dS)
std_agilent_high_dH = np.std(agilent_high_dH)
std_agilent_high_dS = np.std(agilent_high_dS)

#############################################

bird_stx_13_dH = 196
bird_stx_12_dH = 220
bird_stx_11_dH = 267

bird_stx_13_dS = 184
bird_stx_12_dS = 247
bird_stx_11_dS = 326

#############################################
ax1 = plt.axes()

ax1.errorbar(1,mean_stx_11_low_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='b', label='low pressure')
ax1.errorbar(1,mean_stx_11_mid_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='r', label='mid pressure')
ax1.errorbar(1,mean_stx_11_high_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='g', label='high pressure')

ax1.errorbar(2,mean_stx_12_low_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='b')
ax1.errorbar(2,mean_stx_12_mid_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='r')
ax1.errorbar(2,mean_stx_12_high_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='g')

ax1.errorbar(3,mean_stx_13_low_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='b')
ax1.errorbar(3,mean_stx_13_mid_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='r')
ax1.errorbar(3,mean_stx_13_high_dH, std_stx_13_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='g')

ax1.errorbar(4, mean_agilent_high_dH, std_agilent_high_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='c')
ax1.errorbar(4, mean_agilent_low_dH, std_agilent_low_dH, capsize=15, marker='o', markersize=15, linewidth=3, color='m')

ax1.plot(1, bird_stx_11_dH, marker='o', markersize=15, color='k', label='BIRD value')
ax1.plot(2, bird_stx_12_dH, marker='o', markersize=15, color='k')
ax1.plot(3, bird_stx_13_dH, marker='o', markersize=15, color='k')
ax1.plot(4, bird_stx_13_dH, marker='o', markersize=15, color='k')

ax1.set_xticks([1,2,3,4],['Stx 11+','Stx 12+','Stx 13+','45xt Stx 13+'])
ax1.tick_params(axis='both', which='major', labelsize=36)
ax1.set_ylabel(r'$\Delta H^{\ddag}$',fontsize=55)
ax1.set_title(file_name.split(r'/')[-1], fontsize=55)
ax1.legend(fontsize=30)
plt.figure()
###########################################
ax2 = plt.axes()

ax2.errorbar(1,mean_stx_11_low_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='b', label='low pressure')
ax2.errorbar(1,mean_stx_11_mid_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='r', label='mid pressure')
ax2.errorbar(1,mean_stx_11_high_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='g', label='high pressure')

ax2.errorbar(2,mean_stx_12_low_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='b')
ax2.errorbar(2,mean_stx_12_mid_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='r')
ax2.errorbar(2,mean_stx_12_high_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='g')

ax2.errorbar(3,mean_stx_13_low_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='b')
ax2.errorbar(3,mean_stx_13_mid_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='r')
ax2.errorbar(3,mean_stx_13_high_dS, std_stx_13_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='g')

ax2.errorbar(4, mean_agilent_high_dS, std_agilent_high_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='c')
ax2.errorbar(4, mean_agilent_low_dS, std_agilent_low_dS, capsize=15, marker='o', markersize=15, linewidth=3, color='m')

ax2.plot(1, bird_stx_11_dS, marker='o', markersize=15, color='k', label='BIRD value')
ax2.plot(2, bird_stx_12_dS, marker='o', markersize=15, color='k')
ax2.plot(3, bird_stx_13_dS, marker='o', markersize=15, color='k')
ax2.plot(4, bird_stx_13_dS, marker='o', markersize=15, color='k')

ax2.set_xticks([1,2,3,4],['Stx 11+','Stx 12+','Stx 13+','45xt Stx 13+'])
ax2.tick_params(axis='both', which='major', labelsize=36)
ax2.set_ylabel(r'$\Delta S^{\ddag}$',fontsize=55)
ax2.set_title(file_name.split(r'/')[-1], fontsize=55)
ax2.legend(fontsize=30)
plt.figure()


























































