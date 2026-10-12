from svgpathtools import svg2paths
from math import cos , fabs , pi
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close
from svg.path import parse_path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
paths, attributes = svg2paths('Fourier.svg')#getting svg path

for k, v in enumerate(attributes):#parsing path 
    path=parse_path(v['d'])
    break
n=100000#1/dt

p=[(p) for p in (path.point(i/n) for i in range(0,n+1))]#getting the points out
p=np.conj(p)#makes it the corect way round


'''ploting the origonal svg'''
pts=[(p.real,p.imag)for p in (p)]#getting real and imaganry parts for plotting on cartiesian plot
plt.plot(*zip(*pts))
plt.savefig('svgdraw')#saving the figure
plt.show()

k=150# order
c=[]#holding the constants
'''genorating the constants'''
for order in range(-k,k):
    cn=0
    print(order,'constant')
    for i in range(n+1):
        cn=cn+(p[i]*np.exp(-2*np.pi*order*1j*(i/n))*(1/n))
        
    
    c.append(cn)
f=[]#holdding the created function
'''creating the function from the fourier transform'''
for i in range(n+1):
    
        
    ft=0
    for order in range(-k,k):   
       ft=ft+(c[order+k]*np.exp(2*np.pi*order*1j*(i/n)))
       #print(ft)
    f.append(ft)

fl=[(l.real,l.imag) for l in (f)]#getting real and imaganry parts for plotting on cartiesian plot

'''plotting and saving'''
plt.plot(*zip(*fl))
plt.savefig('fourdraw')
plt.show()
