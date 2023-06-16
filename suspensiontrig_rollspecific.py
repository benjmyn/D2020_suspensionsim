
import math
import time


#Math and Inputs

#Chassis Lower
lcha_x = 12
lcha_y = 6
#Chassis Upper
a = 16
b = 14
#Wheel Lower
c = 24
d = 5
#Wheel Upper
tsus_x = 24
tsus_y = 15

heaveON = True
rollON = True
printout = True
guidelines = True

print('Input Bump Travel in Inches')
travel = float(input())
print('Input CW Roll in Inches')
roll = float(input())

if travel > 0 or travel < 0:
	heaveON = True
	print('heaveON = True')
else:
	heaveON = False
	print('heaveON = False')
	
if roll > 0 or roll < 0:
	rollON = True
	print('rollON = True')
else:
	rollON = False
	print('rollON = False')
	

wheeloffset = 0
#wheel line is offset from hub line by this much

link_bottom = math.sqrt((c - lcha_x)**2 + (d - lcha_y)**2)

#Rad0 is Top Susp Linkage, Rad1 is hub point-to-point
rad0 = math.sqrt((tsus_x - a)**2 + (tsus_y - b)**2)  
rad1 = math.sqrt((tsus_x - c)**2 + (tsus_y - d)**2)  

if heaveON == True:
	#All for heave math
	wb__y = d + travel #Wheel-side Bottom (y) after Travel
	wb__x = math.sqrt((link_bottom)**2 - (wb__y-lcha_y)**2)+lcha_x #Wheel-side Bottom (x) after Travel
	D = math.sqrt((wb__x - a)**2 + (wb__y - b)**2) #Distance between rad0 center and rad1 center
	alpha = math.sqrt((D + rad0 + rad1) * (D + rad0 - rad1) * (D - rad0 + rad1) * (-D + rad0 + rad1)) / 4

	pointx1 = (a + wb__x)/2 + ((wb__x - a) * (rad0**2 - rad1**2)) / (2*D**2) + 2*alpha*((b - wb__y) / (D**2))
	#pointx2 = (a + wb__x)/2 + ((wb__x - a) * (rad0**2 - rad1**2)) / (2*D**2) - 2*alpha*((b - wb__y) / (D**2))
	
	#pointy1 = (b + wb__y)/2 + ((wb__y - b) * (rad0**2 - rad1**2)) / (2*D**2) + 2*alpha*((a - wb__x) / (D**2))
	pointy2 = (b + wb__y)/2 + ((wb__y - b) * (rad0**2 - rad1**2)) / (2*D**2) - 2*alpha*((a - wb__x) / (D**2))
	
else:
	wb__y = d
	wb__x = c
	pointx1 = tsus_x
	pointy2 = tsus_y
	D = math.sqrt((wb__x - a)**2 + (wb__y - b)**2) #Distance between rad0 center and rad1 center
	alpha = math.sqrt((D + rad0 + rad1) * (D + rad0 - rad1) * (D - rad0 + rad1) * (-D + rad0 + rad1)) / 4
#Done

#Heave Camber
camber = -math.tan((wb__x - pointx1)/(pointy2 - wb__y))

#Roll Center Location -- this is where it starts getting bad

#ULm = (b - pointy2)/(a - pointx1)
#LLm = (lcha_y - wb__y)/(lcha_x - wb__x)
#ULb = lcha_y - ULm*lcha_x
#LLb = b - ULm*a
#swingpt_x = (ULb - LLb)/(LLm - ULm)
#swingpt_y = (ULb*LLm - LLb*ULm)/(LLm - ULm)
#HUBm = (pointy2 - wb__y)/(pointx1 - wb__x)
#offsetdist = wheeloffset 
#X Intercept
#wheelcontact = -(pointy2 - HUBm*pointx1 + offsetdist)/HUBm 
#trackwidth = 2*wheelcontact


#( (x2*y1 - x1*y2)*(x4-x3) - (x4*y3 - x3*y4)*(x2-x1) ) / ( (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1) )
#( (x2*y1 - x1*y2)*(y4-y3) - (x4*y3 - x3*y4)*(y2-y1) ) / ( (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1) )

swingpt_x = ( (pointx1*b - a*pointy2)*(wb__x-lcha_x) - (wb__x*lcha_y - lcha_x*wb__y)*(pointx1-a) ) / ( (pointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(pointy2-b) )
swingpt_y = ( (pointx1*b - a*pointy2)*(wb__y-lcha_y) - (wb__x*lcha_y - lcha_x*wb__y)*(pointy2-b) ) / ( (pointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(pointy2-b) )

if (wb__x - pointx1) != 0: 
	wheelcontactM = ((wb__y - pointy2) / (wb__x - pointx1))
	wheelcontactX = -(pointy2 - wheelcontactM*pointx1)/ wheelcontactM
else:
	wheelcontactX = pointx1
trackwidth = 2*wheelcontactX

#rollcenterY = -(swingpt_y / ((2*swingpt_x)/wheelcontactX))
rollcenterY = swingpt_y - swingpt_x*(0-swingpt_y)/(wheelcontactX-swingpt_x)

#rc_y = -(wheelcontact*(swingpt_y-0)) / (swingpt_x-wheelcontact)

if printout == True:
	print('Alpha Value: %s' % alpha)
	print(' ')
	print('Lower Wheel-side: (%s, %s)' % (wb__x, wb__y))
	print('Upper Wheel-side: (%s, %s)' % (pointx1, pointy2))
	print('Lower Chassis-side: (%s, %s)' % (lcha_x, lcha_y))
	print('Upper Chassis-side: (%s, %s)' % (a, b))
	print(' ')
	print('Camber: %s' % camber)
	print(' ')
	print('Track Width: %s' % trackwidth)
	print('Swing Point: (%s, %s)' % (swingpt_x, swingpt_y))
	print(' ')
	print('Wheel Contact Point: (%s, %s)' % (wheelcontactX, 0))
	print(' ')
	print('Roll Center: (%s, %s)' % (0, rollcenterY))
	print(' ')
	#print('Roll Center Height: %s' % rc_y)
#Done

#Tkinter -----------------------------------------------------------------------

windowsize = 800 #int(input())

import tkinter
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=int(windowsize), height=int(windowsize))
canvas.pack()

bloop = 0
naptime = 1/60
sf = 18
speed = 1/40

orx = windowsize/2 - 150 #X Origin relative to NW
ory = windowsize/2 + 150 #Y Origin relative to NW (reversed)
ground1 = canvas.create_line(0,ory,windowsize,ory)
halfline = canvas.create_line(orx, 0, orx, windowsize, dash=(5,))

carframe = canvas.create_polygon(orx + sf*a,   ory - sf*b,   orx + sf*lcha_x,   ory - sf*lcha_y,   orx - sf*lcha_x,   ory - sf*lcha_y,  orx - sf*a,  ory - sf*b, fill = 'white', outline='blue')



#Suspension Linkages
uppr = canvas.create_line(orx, ory, 500, 250)
lowr = canvas.create_line(orx, ory, 500, 250)
hub = canvas.create_line(orx, ory, 500, 250)




#Circle to assure constant hub size
if guidelines == True:
	circuul = canvas.create_oval(orx, ory, 500, 250, dash = (3,))
	vertcheckinner = canvas.create_line(orx + sf*a, 0, orx + sf*a, 800, fill='red')
	vertcheckouter = canvas.create_line(orx + sf*lcha_x, 0, orx + sf*lcha_x, 800, fill='red')
	contactpatch = canvas.create_oval(orx+sf*wheelcontactX + 10, ory - 10, orx+sf*wheelcontactX - 10, ory + 10)
	lowlinkline = canvas.create_line(orx+sf*wb__x,ory-sf*wb__y,   orx+sf*swingpt_x,ory-sf*swingpt_y, fill='green')
	upplinkline = canvas.create_line(orx+sf*pointx1,ory-sf*pointy2,  orx+sf*swingpt_x,ory-sf*swingpt_y, fill='green')
	rollline = canvas.create_line(orx+sf*pointx1,ory-sf*pointy2,  orx+sf*swingpt_x,ory-sf*swingpt_y, fill='green')
	rollcentercircle = canvas.create_oval(orx+10,ory-sf*rollcenterY+10,  orx-10,ory-sf*rollcenterY-10, dash = (1,))
	

#Text
camberlabel = canvas.create_text(200, 250, text=('Camber: %s' % round(math.degrees(camber), 3)))

#Heave Animation
if heaveON == True and rollON == False:
	while bloop < 36000000:
		travel2 = (travel/2)*math.cos((math.pi*bloop)*speed+math.pi) + (travel/2)
		
		adjwb__y = d + travel2 #d
		adjwb__x = math.sqrt((link_bottom)**2 - (adjwb__y-lcha_y)**2)+lcha_x #c
		
		Dtwelve = math.sqrt((adjwb__x - a)**2 + (adjwb__y - b)**2)
		wsixteen = math.sqrt((Dtwelve + rad0 + rad1) * (Dtwelve + rad0 - rad1) * (Dtwelve - rad0 + rad1) * (-Dtwelve + rad0 + rad1)) / 4

		
		adjpointx1 = (a + adjwb__x)/2 + ((adjwb__x - a) * (rad0**2 - rad1**2)) / (2*Dtwelve**2) + 2*wsixteen*((b - adjwb__y) / (Dtwelve**2)) #pointx1
		adjpointy2 = (b + adjwb__y)/2 + ((adjwb__y - b) * (rad0**2 - rad1**2)) / (2*Dtwelve**2) - 2*wsixteen*((a - adjwb__x) / (Dtwelve**2)) #tsus_y
		
		
		adjswingpt_x = ( (adjpointx1*b - a*adjpointy2)*(wb__x-lcha_x) - (wb__x*lcha_y - lcha_x*wb__y)*(adjpointx1-a) ) / ( (adjpointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(adjpointy2-b) )
		adjswingpt_y = ( (adjpointx1*b - a*adjpointy2)*(wb__y-lcha_y) - (wb__x*lcha_y - lcha_x*wb__y)*(adjpointy2-b) ) / ( (adjpointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(adjpointy2-b) )
		
		if (adjwb__x - adjpointx1) != 0: 
			#adjwheelcontactM = ((wb__y - adjpointy2) / (wb__x - adjpointx1))
			adjwheelcontactM = ((d - tsus_y) / (adjwb__x - adjpointx1))
			#adjwheelcontactX = -(adjpointy2 - adjwheelcontactM*adjpointx1)/ adjwheelcontactM
			adjwheelcontactX = -(tsus_y - adjwheelcontactM*adjpointx1)/ adjwheelcontactM
		else:
			adjwheelcontactX = adjpointx1
		
		
		#canvas.coords(lowr, orx + sf*lcha_x, ory - sf*lcha_y, orx + sf*adjwb__x, ory - sf*adjwb__y)
		canvas.coords(lowr, orx + sf*lcha_x, ory - sf*(lcha_y - travel2), orx + sf*adjwb__x, ory - sf*d)
		#canvas.coords(uppr, orx + sf*a, ory - sf*b, orx + sf*adjpointx1, ory - sf*adjpointy2)
		canvas.coords(uppr, orx + sf*a, ory - sf*(b - travel2), orx + sf*adjpointx1, ory - sf*tsus_y)
		
		
		if guidelines == True:
			#canvas.coords(circuul, orx + sf*(adjwb__x + rad1),  ory - sf*(adjwb__y - rad1),  orx + sf*(adjwb__x - rad1),  ory - sf*(adjwb__y + rad1))
			#Circle follows adjusted
			canvas.coords(circuul, orx + sf*(adjwb__x + rad1), ory - sf*(d - rad1), orx + sf*(adjwb__x - rad1), ory - sf*(d + rad1))
			canvas.coords(contactpatch, orx+sf*adjwheelcontactX + 10, ory - 10, orx+sf*adjwheelcontactX - 10, ory + 10)
			
			#Roll and Swing Center
			#swingpt_x = ( (pointx1*b - a*pointy2)*(wb__x-lcha_x) - (wb__x*lcha_y - lcha_x*wb__y)*(pointx1-a) ) / ( (pointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(pointy2-b) )
			#swingpt_y = ( (pointx1*b - a*pointy2)*(wb__x-lcha_x) - (wb__x*lcha_y - lcha_x*wb__y)*(pointy2-b) ) / ( (pointx1-a)*(wb__y-lcha_y) - (wb__x-lcha_x)*(pointy2-b) )
			
			PT_Ax = (adjpointx1*(b-travel2) - a*tsus_y)*(adjwb__x - lcha_x)
			PT_Ay = (adjpointx1*(b-travel2) - a*tsus_y)*(d - (lcha_y - travel2))
			#		(pointx1*b - a*pointy2)*(wb__x-lcha_x)
			#		(pointx1*b - a*pointy2)*(wb__x-lcha_x)
			
			PT_Bx = (adjwb__x*(lcha_y - travel2) - lcha_x*d)*(adjpointx1 - a)
			PT_By = (adjwb__x*(lcha_y - travel2) - lcha_x*d)*(tsus_y - (b - travel2))
			#		(wb__x*lcha_y - lcha_x*wb__y)*(pointx1-a)
			#		(wb__x*lcha_y - lcha_x*wb__y)*(pointy2-b)
			
			PT_C = (pointx1-a) * (d - (lcha_y - travel2))
			#		(pointx1-a) * (wb__y - lcha_y)
			PT_D = (adjwb__x-lcha_x) * (tsus_y - (b - travel2))
			#		(wb__x-lcha_x) * (pointy2-b)
			
			adjswingpt_x = (PT_Ax - PT_Bx) / (PT_C - PT_D)
			adjswingpt_y = (PT_Ay - PT_By) / (PT_C - PT_D)
			canvas.coords(lowlinkline,orx+sf*adjwb__x,ory-sf*d,   orx+sf*adjswingpt_x,ory-sf*adjswingpt_y)
			canvas.coords(upplinkline,orx+sf*adjpointx1,ory-sf*tsus_y,  orx+sf*adjswingpt_x,ory-sf*adjswingpt_y)
			
			adjrollcenterY = adjswingpt_y - adjswingpt_x*(0-adjswingpt_y)/(adjwheelcontactX-adjswingpt_x)
			canvas.coords(rollline,orx+sf*adjswingpt_x,ory-sf*adjswingpt_y,  orx+sf*adjwheelcontactX,ory)
			canvas.coords(rollcentercircle, orx+10,ory-sf*adjrollcenterY+10,  orx-10,ory-sf*adjrollcenterY-10)
			
		#canvas.coords(hub, orx + sf*adjwb__x, ory - sf*adjwb__y, orx + sf*adjpointx1, ory - sf*adjpointy2)
		canvas.coords(hub, orx + sf*adjwb__x, ory - sf*d, orx + sf*adjpointx1, ory - sf*tsus_y) #Y does not change--chassis moves instead
		
		canvas.coords(carframe, orx + sf*a,   ory - sf*(b - travel2),   orx + sf*lcha_x,   ory - sf*(lcha_y - travel2),   orx - sf*lcha_x,   ory - sf*(lcha_y - travel2),  orx - sf*a,  ory - sf*(b - travel2))
		
		orx+10,ory-sf*rollcenterY+10,  orx-10,ory-sf*rollcenterY-10
		
		bloop = bloop + 1
		tk.update()
		time.sleep(naptime)
	print('Done Heave!')

#elif rollON == True:
#	while bloop < 36000000:
		
		#Do this
		
#Done
#else:
#	print('Roll and Heave are off.')
#Done