'''
Name: Pragyan Mehrotra
Roll No: 2018168
Section: A
Group: 8
'''


import matplotlib.pyplot as plt	
import random
from math import *
plt.ion()

#to randomly select a color so that the output stays fresh
def color_select():
	s='#'
	for i in range(6):
		x = hex(random.randint(0,15))[2:]
		s+=x
	return s

#draws a polygon given the list of coordinates
def draw_poly(x,y,objcolor):
	plt.plot(x+[x[0]],y+[y[0]],color=objcolor)

#draws a disc given center and the radius
def ddftft(x,y,r,objcolor):
	x_=[]
	y_=[]
	x1 = x+r
	y1 = y
	theta = 0.0
	dtheta = 1*pi/180
	while theta < 2*pi:
		theta += dtheta
		x_.append(x1)
		y_.append(y1)
		x2 = x + r*cos(theta)
		y2 = y + r*sin(theta)
		#print (x1)
		x1 = x2
		y1 = y2
	draw_poly(x_,y_,objcolor)
	return x_,y_	
	
#multiplies 2 arbitrary matrices
def matrix_multiplication(a,b):
	m = []
	if len(a[0]) != len(b):
		return
	for i in range(len(a)):
		c=0
		r=[]
		while c != len(b[0]):
			elem = 0
			for j in range(len(a[i])):
				elem += a[i][j]*b[j][c]
			c+=1
			r.append(elem)
		m.append(r)	
	return m

#performs the scaling operation
def scale(x,y,sx,sy):
	scale_matrix = [[sx,0,0],[0,sy,0],[0,0,1]]
	coord_matrix = [[x],[y],[1]]
	g = matrix_multiplication(scale_matrix,coord_matrix)
	x_ = g[0][0]
	y_ = g[1][0]
	return x_,y_

#performs the rotation operation phi is given in degrees
def rotate(x,y,phi):
	phi = phi * pi/180
	rot_matrix = [[cos(phi),-1*sin(phi),0],[sin(phi),cos(phi),0],[0,0,1]]
	coord_matrix = [[x],[y],[1]]
	g = matrix_multiplication(rot_matrix,coord_matrix)
	x_ = g[0][0]
	y_ = g[1][0]
	return x_,y_

#performs the transformation operation						
def transform(x,y,dx,dy):
	trans_matrix = [[1,0,dx],[0,1,dy],[0,0,1]]
	coord_matrix = [[x],[y],[1]]
	g = matrix_multiplication(trans_matrix,coord_matrix)
	x_ = g[0][0]
	y_ = g[1][0]
	return x_,y_

s=''
figure = ''

while s != 'quit':
	s = input()
	s = s.lower()
	if s=='quit':
		break
	if s=='polygon':
		figure = s
		objcolor = color_select()
	if s=='disc':
		figure = s
		objcolor = color_select()
	if figure=='polygon':
		if s=='polygon':
			x = list(map(float, input().split()))
			y = list(map(float, input().split()))
			objcolor = color_select()
			draw_poly(x,y,objcolor)
		else:
			a= s.split()
			if a[0].lower() == 't':
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = transform(x[i],y[i],float(a[1]),float(a[2]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				#plt.clf()
				print (''.join(str(i)+' ' for i in x))
				print (''.join(str(i)+' ' for i in y))
				draw_poly(x,y,objcolor)
			if a[0].lower() == 's':
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = scale(x[i],y[i],float(a[1]),float(a[2]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				#plt.clf()
				print (''.join(str(i)+' ' for i in x))
				print (''.join(str(i)+' ' for i in y))
				draw_poly(x,y,objcolor)
			if a[0].lower() == 'r':
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = rotate(x[i],y[i],float(a[1]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				#plt.clf()
				print (''.join(str(i)+' ' for i in x))
				print (''.join(str(i)+' ' for i in y))
				draw_poly(x,y,objcolor)
	if figure == 'disc':
		if s=='disc':
			cx,cy,r = map(float, input().split())
			r1 = r
			r2 = r
			objcolor = color_select()
			x,y = ddftft(cx,cy,r,objcolor)
		else:	
			a = s.split()
			if a[0].lower() == 't':
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = transform(x[i],y[i],float(a[1]),float(a[2]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				cx,cy = transform(cx,cy,float(a[1]),float(a[2]))
				print (str(cx) + ' ' + str(cy) + ' ' + str(r1) + ' ' + str(r2))
				draw_poly(x,y,objcolor)
			if a[0].lower() == 's':
				r1 = float(a[1])*r1
				r2 = float(a[2])*r2
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = scale(x[i],y[i],float(a[1]),float(a[2]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				print (str(cx) + ' ' + str(cy) + ' ' + str(r1) + ' ' + str(r2))
				draw_poly(x,y,objcolor)
			if a[0].lower() == 'r':
				new_x = []
				new_y = []
				for i in range(len(x)):
					x_,y_ = rotate(x[i],y[i],float(a[1]))
					new_x.append(x_)
					new_y.append(y_)
				x = new_x
				y = new_y
				print (str(cx) + ' ' + str(cy) + ' ' + str(r1) + ' ' + str(r2))
				draw_poly(x,y,objcolor)


