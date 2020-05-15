import turtle
import numpy as np
import time

a = 5
b = 0.3063489
N = 1000
theta = np.linspace(0, 5*np.pi, N)

x = a*np.exp(b*theta)*np.cos(theta)
y = a*np.exp(b*theta)*np.sin(theta)

for elem in zip(x,y):
	turtle.goto(elem[0], elem[1])
	#time.sleep(0.050)