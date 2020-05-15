"""
Proyecto 2: Determinación de áreas por método  Monte-Carlo
"""
# %%
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#%%

f = lambda x: 1-x**2
g = lambda x: -x+1

x = np.linspace(0,1,num=1000)
yf = f(x)
yg = g(x)

xr = np.random.random(1000)
yr = np.random.random(1000)
#%%

fig, ax = plt.subplots()
ax.plot(x,yf,linewidth=3,label='$f(x)=1-x^2$')
ax.plot(x,yg,linewidth=3,label='$g(x)=-x+1$')
plt.legend(loc='upper right', frameon=True)
plt.scatter(xr, yr, c='red',s=1)
plt.xlim(0,1)
plt.ylim(0,1)
ax.fill_between(x, yf, yg, where=yf >= yg, facecolor='grey', interpolate=True,\
                alpha = 0.25)
plt.savefig('mc.png',dpi=300)

