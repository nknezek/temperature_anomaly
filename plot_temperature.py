# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:53:01 2016

@author: nknezek
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#%%
filename = 'HadCRUT4-gl.dat'
data = np.genfromtxt(filename, usecols=range(13))
real_data = data[::2,:]
years = np.array(real_data[:,0], dtype='int')
clean_data = np.reshape(real_data[:,1:], (-1,1))
clean_data = clean_data[:-9]
#%%
#theta = np.array(range(len(clean_data)))*np.pi*2./12. % (2*np.pi)-np.pi/6
#pre_industrial = np.mean(clean_data[:12*50])
#
#C = 120
#adjust0 = 1.5
#cmap = matplotlib.cm.get_cmap('jet')
#ax = plt.subplot(111, projection='polar')
#
#ax.set_rgrids([x+adjust0 for x in [-0.5, 0.0, 0.5, 1., 1.5, 2.]], labels = ['-0.5', '0.0', '+0.5', '+1.0', '+1.5', '+2.0'])
#ax.set_thetagrids(np.linspace(0,360.,12, endpoint=False),labels=reversed(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']))
#for i in range(1,17):
#    ax.plot(-theta[(i-1)*C:i*C], clean_data[(i-1)*C:i*C]+adjust0-pre_industrial, color=cmap((i-1)/15))
#ax.plot(np.linspace(0,2*np.pi, 100, endpoint=True), [adjust0+2.]*100, color='red',linewidth=3.)
#ax.set_rlim([0.,2.25+adjust0])
#ax.set_theta_zero_location('N')
#ax.legend()
#%%
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

fig = plt.figure(figsize=(8,6))
ims = []
theta = np.array(range(len(clean_data)))*np.pi*2./12. % (2*np.pi)
pre_industrial = np.mean(clean_data[:12*50])

adjust0 = 1.5
cmap = matplotlib.cm.get_cmap('jet')
ax = plt.subplot(111, projection='polar')
ax.set_rgrids([x+adjust0 for x in [-0.5, 0.0, 0.5, 1., 1.5, 2.]], labels = ['-0.5', '0.0', '+0.5', '+1.0', '+1.5', '+2.0'])
ax.set_thetagrids(np.linspace(0,360.,12, endpoint=False),labels=reversed(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan']))
ax.plot(np.linspace(0,2*np.pi, 100, endpoint=True), [adjust0+2.]*100, color='red',linewidth=3.)
ax.set_rlim([0.,2.25+adjust0])
ax.set_theta_zero_location('N')

for j in range(1,168):
    for i in range(1,j+1):
        ax.plot(-theta[(i-1)*12:i*12+1],clean_data[(i-1)*12:i*12+1]+adjust0-pre_industrial, color=cmap(i/158))
    a = list(ax.lines)
    t = ax.text(1.85,0.72,str(years[j-1]), size=24)
    im = a+[t]
    ims.append(im)
    

ax.set_rlim([0.,2.25+adjust0])
ax.set_theta_zero_location('N')
im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000,
                                   blit=True)
im_ani.save('Global_T_anomaly.mp4',writer=writer)

