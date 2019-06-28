# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:49:08 2019

@author: LC
"""

'''
illustration for subplot with three methods
'''

import numpy as np 
import matplotlib.pyplot as plt 

## define the array for plotting 
x    = np.linspace(-1,1,50)
y    = np.random.normal(0,1,np.size(x))

## method 1 
plt.figure(num=1)
plt.subplot(2,1,1) ## the 1st of the 2*1 
plt.plot(x,y,'g-^')
plt.title('(a) method1 subplot')

plt.subplot(2,3,4) ## the 4th location of 2*3 
plt.plot(x,np.abs(y),'b-')

plt.subplot(235) ## the 5th location of 2*3 
plt.plot(x,y**2,'r-')

plt.subplot(236) ## the 6th location of 2*3 
plt.plot(x,np.sin(np.pi*y),'k--')
plt.savefig('liuc_subplot1.eps')


## method2 
plt.figure(num=2)
# 3*3 girds, the 1st location 
ax1 = plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3) 
ax1.plot(x,y,'g-')
ax1.set_title('method2 subplot2gird')
# 3*3 grid the 2rd location 
ax2= plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=2)
ax2.plot(x,y,'ro')

ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2,colspan=1)
ax3.plot(x,np.abs(y))

ax4 = plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=1)
ax4.plot(x,y**2)

ax5 = plt.subplot2grid((3,3),(2,1))
ax5.plot(y,x)
plt.savefig('liuc_subplot2.eps')


## method3 
import matplotlib.gridspec as gridspec
plt.figure(num=3)
gs  = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax1.set_title('method3 girdspec')
ax1.plot(x,y,'g-')

ax2 = plt.subplot(gs[1,0:2])
ax2.plot(x,y,'ro')

ax3 = plt.subplot(gs[1:3,2])
ax3.plot(y,np.sqrt(x))

ax4 = plt.subplot(gs[2,0:1])
ax4.scatter(x,y)

# the 2nd to 3rd (not include) column 
ax5 = plt.subplot(gs[2,1:2]) 
ax5.plot(x,2*y)
plt.savefig('liuc_subplot3.eps')


## method4 
fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,sharey=True)
ax1.plot(x,y)
ax1.set_title('method4 subplots')
ax1.set_ylim(-3,3)

ax2.scatter(x,y)

plt.savefig('liuc_subplot4.eps')
plt.show()




