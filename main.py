import random
import numpy as np
from discreteMarkovChain import markovChain
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def bar(p):
	return 1-p

def M1(p1_p,p2_p):
	(pc,pd)=p1_p
	(qc,qd)=p2_p

	m=[]
	for initial_s in ['CC','CD','DC','DD']:
		row=[]
		for final_s in ['CC','CD','DC','DD']:
			if initial_s[1]=='C':
				p=pc
			else:
				p=pd
			if initial_s[0]=='C':
				q=qc
			else:
				q=qd

			if final_s[0]!='C':
				p=bar(p)
			if final_s[1]!='C':
				q=bar(q)

			row.append(p*q)

		m.append(row)

	return np.array(m)

def point(p1_p,p2_p):
	P = M1(p1_p,p2_p)
	mc = markovChain(P)
	mc.computePi('linear') #We can also use 'power', 'krylov' or 'eigen'
	return mc.pi



fig = plt.figure()
ax = plt.axes(projection='3d')

ax = plt.axes(projection='3d')

zdata=[]
xdata=[]
ydata=[]
for i in range(1000):
	p1_p=(random.random(),random.random())
	p2_p=(random.random(),random.random())

	# Data for three-dimensional scattered points
	zdata.append(point(p1_p,p2_p)[0])
	xdata.append(p1_p[0]*p1_p[1])
	ydata.append(p2_p[0]*p2_p[1])
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

plt.show()