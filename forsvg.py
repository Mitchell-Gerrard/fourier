from svgpathtools import svg2paths
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

k=300# order
c=[]#holding the constants
'''genorating the constants'''
for order in range(-k,k):
    cn=0

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

'''animating the Fourier reconstruction'''
fig, ax = plt.subplots()
ax.plot(*zip(*pts), color='lightgray', label='Original SVG')
animated_line, = ax.plot([], [], color='black', label='Fourier reconstruction')
ax.set_aspect('equal')
all_points = pts + fl
ax.set_xlim(min(point[0] for point in all_points), max(point[0] for point in all_points))
ax.set_ylim(min(point[1] for point in all_points), max(point[1] for point in all_points))
ax.legend()

frame_indices = np.unique(np.linspace(2, len(fl), 300, dtype=int))

def update(frame):
    animated_line.set_data(*zip(*fl[:frame]))
    return animated_line,

animation = FuncAnimation(
    fig,
    update,
    frames=frame_indices,
    interval=20,
    blit=True,
    repeat=True,
)
save_path = 'fourier_animation.mp4'
animation.save(save_path, writer='ffmpeg', fps=30)
plt.show()
