
import math
import time


#Math and inputs -----------------------------------------------------------------------

print('Input the x position of the chassis-side LOWER suspension point in inches.')
lcha_x = 12 #int(input()) #12
print('Input the y position of the chassis-side LOWER suspension point in inches.')
lcha_y = 6 #int(input()) #6

print('Input the x position of the chassis-side UPPER suspension point in inches.')
a = 16 #int(input()) #x of circle0 #16
print('Input the y position of the chassis-side UPPER suspension point in inches.')
b = 14 #14 #int(input()) #y of circle0 #14

print('Input the x position of the wheel-side LOWER suspension point in inches.')
c = 24 #int(input()) #x of circle1 #32
print('Input the y position of the wheel-side LOWER suspension point in inches.')
d = 5 #int(input()) #y of circle1 #5

print('Input the x position of the wheel-side UPPER suspension point in inches.')
tsus_x = 24 #int(input()) #32
print('Input the y position of the wheel-side UPPER suspension point in inches.')
tsus_y = 15 #int(input()) #15

print('Input your desired vertical travel in inches.')
travel = float(input())

link_bottom = math.sqrt((c - lcha_x)**2 + (d - lcha_y)**2)
print(link_bottom)

wb__y = d + travel #Wheel-side Bottom (y) after Travel
wb__x = math.sqrt((link_bottom)**2 - (wb__y-lcha_y)**2)+lcha_x #Wheel-side Bottom (x) after Travel
print(wb__y)
print(wb__x)


D = math.sqrt((wb__x - a)**2 + (wb__y - b)**2) #distance between centers

rad0 = math.sqrt((tsus_x - a)**2 + (tsus_y - b)**2)  #Top suspension linkage
rad1 = math.sqrt((tsus_x - c)**2 + (tsus_y - d)**2)  #Hub point-to-point



#print(' ')
#print(a)
#print(b)
#print(c)
#print(d)
print(' ')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(' ')
print('Distance between circle centers:')
print(D)
print(' ')
print('Radius of Upper Suspension Arm:')
print(rad0)
print('Radius of Hub Linkage:')
print(rad1)
print(' ')

print('Alpha value:')
w = math.sqrt((D + rad0 + rad1) * (D + rad0 - rad1) * (D - rad0 + rad1) * (-D + rad0 + rad1)) / 4
print(w)
print(' ')


pointx1 = (a + wb__x)/2 + ((wb__x - a) * (rad0**2 - rad1**2)) / (2*D**2) + 2*w*((b - wb__y) / (D**2))
pointx2 = (a + wb__x)/2 + ((wb__x - a) * (rad0**2 - rad1**2)) / (2*D**2) - 2*w*((b - wb__y) / (D**2))

pointy1 = (b + wb__y)/2 + ((wb__y - b) * (rad0**2 - rad1**2)) / (2*D**2) + 2*w*((a - wb__x) / (D**2))
pointy2 = (b + wb__y)/2 + ((wb__y - b) * (rad0**2 - rad1**2)) / (2*D**2) - 2*w*((a - wb__x) / (D**2))

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(' ')

print('Lower Wheel-side: (%s, %s)' % (wb__x, wb__y))
print('Upper Wheel-side: (%s, %s)' % (pointx1, pointy2))
print('Lower Chassis-side: (%s, %s)' % (lcha_x, lcha_y))
print('Upper Chassis-side: (%s, %s)' % (a, b))
#print(pointx1) #31.749 #Important
#print(pointx2) #24.487
#print(pointy1) #0.4
#print(pointy2) #16.997 #Important
print(' ')

camber = -math.tan((wb__x - pointx1)/(pointy2 - wb__y))
print(camber)


print(' ')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('Tkinter:')

#Tkinter -----------------------------------------------------------------------
print('Input your window size in pixels.')
windowsize = 800 #int(input())
print('Please wait.')

import tkinter
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=int(windowsize), height=int(windowsize))
canvas.pack()


bloop = 36000000 #0
naptime = 1/60
sf = 15 #Scale Factor

speed = 1/40

orx = windowsize/2 - 150
ory = windowsize/2 + 150
ground1 = canvas.create_line(0,ory,windowsize,ory)
halfline = canvas.create_line(orx, 0, orx, windowsize, dash=(5,))

carframe = canvas.create_polygon(orx + sf*a,   ory - sf*b,   orx + sf*lcha_x,   ory - sf*lcha_y,   orx - sf*lcha_x,   ory - sf*lcha_y,  orx - sf*a,  ory - sf*b, fill = 'white', outline='blue')

uppr = canvas.create_line(orx, ory, 500, 250)
lowr = canvas.create_line(orx, ory, 500, 250)
hub = canvas.create_line(orx, ory, 500, 250)


circuul = canvas.create_oval(orx, ory, 500, 250, dash = (3,))

while bloop < 36000000: #For Heave
	#bruh = 50*math.sin(bloop*naptime)
	#cruh = 50*math.cos(bloop*naptime)
	#canvas.create_line(windowsize/2 + bruh, windowsize/2 - cruh, 500, 250)
	
	travel2 = (travel/2)*math.cos((math.pi*bloop)*speed+math.pi) + (travel/2)
	
	
	
	adjwb__y = d + travel2 #d
	adjwb__x = math.sqrt((link_bottom)**2 - (adjwb__y-lcha_y)**2)+lcha_x #c
	
	Dtwelve = math.sqrt((adjwb__x - a)**2 + (adjwb__y - b)**2)
	wsixteen = math.sqrt((Dtwelve + rad0 + rad1) * (Dtwelve + rad0 - rad1) * (Dtwelve - rad0 + rad1) * (-Dtwelve + rad0 + rad1)) / 4

	
	adjpointx1 = (a + adjwb__x)/2 + ((adjwb__x - a) * (rad0**2 - rad1**2)) / (2*Dtwelve**2) + 2*wsixteen*((b - adjwb__y) / (Dtwelve**2)) #tsus_x
	adjpointy2 = (b + adjwb__y)/2 + ((adjwb__y - b) * (rad0**2 - rad1**2)) / (2*Dtwelve**2) - 2*wsixteen*((a - adjwb__x) / (Dtwelve**2)) #tsus_y

	
	canvas.coords(lowr, orx + sf*lcha_x, ory - sf*lcha_y, orx + sf*adjwb__x, ory - sf*adjwb__y)
	canvas.coords(uppr, orx + sf*a, ory - sf*b, orx + sf*adjpointx1, ory - sf*adjpointy2)
	canvas.coords(circuul, orx + sf*(adjwb__x + rad1),  ory - sf*(adjwb__y - rad1),  orx + sf*(adjwb__x - rad1),  ory - sf*(adjwb__y + rad1))
	
	canvas.coords(hub, orx + sf*adjwb__x, ory - sf*adjwb__y, orx + sf*adjpointx1, ory - sf*adjpointy2)
	
	bloop = bloop + 1
	tk.update()
	time.sleep(naptime)
print("Done Heave!")



