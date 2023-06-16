
import math
import time

coords_decimals = 3    #Rounding for Coordinates
guidelines = True      #Circular Distance Guidelines in Tkinter
CCWanimation = True    #Counter-clockwise Animation

#----------Tkinter Setup-----------
import tkinter 
from tkinter import *

tk = Tk()
windowsize_x = 800
windowsize_y = 800

canvas = Canvas(tk,
    width = int(windowsize_x),
	height = int(windowsize_y)
	)
canvas.pack()

#---------Body Coordinates---------
loch_x = 12 
loch_y = 6 #Lower Chassis

upch_x = 16
upch_y = 14 #Upper Chassis

lowh_x = 24 
lowh_y = 5 #Lower Wheel

upwh_x = 24
upwh_y = 15 #Upper Wheel

#------------Symmetry--------------
                            #Symmetry is across Y axis
left_loch_xsta = -loch_x    #X is reversed
right_loch_xsta = loch_x
left_loch_ysta = loch_y     #Y is not reversed
right_loch_ysta = loch_y 

left_upch_xsta = -upch_x
right_upch_xsta = upch_x
left_upch_ysta = upch_y
right_upch_ysta = upch_y

left_lowh_xsta = -lowh_x
right_lowh_xsta = lowh_x
left_lowh_ysta = lowh_y
right_lowh_ysta = lowh_y

left_upwh_xsta = -upwh_x
right_upwh_xsta = upwh_x
left_upwh_ysta = upwh_y
right_upwh_ysta = upwh_y

print("--------STATIC BODY COORDS-----------")
print("Upper Chassis: (%s, %s), (%s, %s)" % (left_upch_xsta, left_upch_ysta, right_upch_xsta, right_upch_ysta))
print("Upper Wheel: (%s, %s), (%s, %s)" % (left_upwh_xsta, left_upwh_ysta, right_upwh_xsta, right_upwh_ysta))
print("Lower Chassis: (%s, %s), (%s, %s)" % (left_loch_xsta, left_loch_ysta, right_loch_xsta, right_loch_ysta))
print("Lower Wheel: (%s, %s), (%s, %s)" % (left_lowh_xsta, left_lowh_ysta, right_lowh_xsta, right_lowh_ysta))
print("-------------------------------------")


#---Wishbone and Knuckle Lengths---
lolink = math.sqrt( (loch_x - lowh_x) ** 2 
                     + (loch_y - lowh_y) ** 2
				  )

uplink = math.sqrt( (upch_x - upwh_x) ** 2 
                     + (upch_y - upwh_y) ** 2
				  )

midlink = math.sqrt( (lowh_x - upwh_x) ** 2 
                     + (lowh_y - upwh_y) ** 2
				  )


#---------Body Roll Test-----------
roll_center_x = 0
roll_degrees = 5 #+CCW -CW
roll_radians = math.radians(roll_degrees)


#------Finding Swing Point---------
swing_PTA_xsta = ((right_upwh_xsta*right_upch_ysta 
                 - right_upch_xsta*right_upwh_ysta)
				 *
				 (right_lowh_xsta - right_loch_xsta))
				 
swing_PTA_ysta = ((right_upwh_xsta*right_upch_ysta 
                 - right_upch_xsta*right_upwh_ysta)
				 *
				 (right_lowh_ysta - right_loch_ysta))

swing_PTB_xsta = ((right_lowh_xsta*right_loch_ysta 
                 - right_loch_xsta*right_lowh_ysta)
				 *
				 (right_upwh_xsta - right_upch_xsta))
				 
swing_PTB_ysta = ((right_lowh_xsta*right_loch_ysta 
                 - right_loch_xsta*right_lowh_ysta)
				 *
				 (right_upwh_ysta - right_upch_ysta))

swing_PTCsta = ((right_upwh_xsta - right_upch_xsta)
                 *
				 (right_lowh_ysta - right_loch_ysta)
				 )
swing_PTDsta = ((right_lowh_xsta - right_loch_xsta)
                 *
				 (right_upwh_ysta - right_upch_ysta)
                )
swing_point_xsta = ((swing_PTA_xsta - swing_PTB_xsta) 
                 / 
				 (swing_PTCsta - swing_PTDsta))
				 
swing_point_ysta = ((swing_PTA_ysta - swing_PTB_ysta) 
                 / 
				 (swing_PTCsta - swing_PTDsta))



#------Finding Wheel Contact---------				 
if (right_lowh_xsta - right_upwh_xsta) != 0:     #Solves python error of division by zero

	m_wheel_contactsta = ((right_upwh_ysta - right_lowh_ysta) 
	                     / 
						 (right_upwh_xsta - right_lowh_xsta))
						 
	wheel_contact_xsta = ((right_lowh_ysta - right_lowh_xsta * m_wheel_contactsta) 
	                     / 
						 m_wheel_contactsta)
else:
	wheel_contact_xsta = right_lowh_xsta


#------Finding Wheel Contact---------
m_roll_center = -swing_point_ysta / (wheel_contact_xsta - swing_point_xsta)
roll_center_y = swing_point_ysta - swing_point_xsta*m_roll_center
#roll_center_y = 10
print("(%s, %s)" % (swing_point_xsta, swing_point_ysta))
print("(%s, 0)" % wheel_contact_xsta)


#--------Rotated Coordinates---------

left_loch_x = round(left_loch_xsta * math.cos(roll_radians)
                    - (left_loch_ysta - roll_center_y) * math.sin(roll_radians)
					, coords_decimals)

right_loch_x = round(right_loch_xsta * math.cos(roll_radians)
                    - (right_loch_ysta - roll_center_y) * math.sin(roll_radians)
					, coords_decimals)

left_loch_y = round((left_loch_ysta - roll_center_y) * math.cos(roll_radians)
                    + (left_loch_xsta) * math.sin(roll_radians)
					+ roll_center_y
					, coords_decimals)

right_loch_y = round((right_loch_ysta - roll_center_y) * math.cos(roll_radians)
                    + (right_loch_xsta) * math.sin(roll_radians)
					+ roll_center_y
					, coords_decimals)

left_upch_x = round(left_upch_xsta * math.cos(roll_radians)
                    - (left_upch_ysta - roll_center_y) * math.sin(roll_radians)
					, coords_decimals)

right_upch_x = round(right_upch_xsta * math.cos(roll_radians)
                    - (right_upch_ysta - roll_center_y) * math.sin(roll_radians)
					, coords_decimals)

left_upch_y = round((left_upch_ysta - roll_center_y) * math.cos(roll_radians)
                    + (left_upch_xsta) * math.sin(roll_radians)
					+ roll_center_y
					, coords_decimals)

right_upch_y = round((right_upch_ysta - roll_center_y) * math.cos(roll_radians)
                    + (right_upch_xsta) * math.sin(roll_radians)
					+ roll_center_y
					, coords_decimals)

d_right_losu = ((lolink**2)                    #Partial Derivatives for circle intersection
                - (right_loch_y - lowh_y)**2) 
d_left_losu = ((lolink**2) 
                - (left_loch_y - lowh_y)**2)

right_lowh_x = round(right_loch_x 
                    + math.sqrt(d_right_losu)
					, coords_decimals) #x1

left_lowh_x = round(left_loch_x 
                   - math.sqrt(d_left_losu)
				   , coords_decimals) #x2
				   
left_lowh_y = left_lowh_ysta
right_lowh_y = right_lowh_ysta      #Wheel y's don't change unless tire itself compresses


dist_right_upsu = math.sqrt((right_upch_x - right_lowh_x)**2 
                            + (right_upch_y - right_lowh_y)**2)

d_right_upsu = (0.25 * 
               math.sqrt(
			          (dist_right_upsu + midlink + uplink)
					  *
					  (dist_right_upsu + midlink - uplink)
					  *
					  (dist_right_upsu - midlink + uplink)
					  *
					  (-dist_right_upsu + midlink + uplink)
					  )
			    )          #Partial Derivative

right_upwh_x = round(
                  ((right_lowh_x + right_upch_x) / 2) 
				  + 
				  (  ((right_upch_x - right_lowh_x)*(midlink**2 - uplink**2))
				    /
				     (2*(dist_right_upsu**2))  ) 
				  - (2 * d_right_upsu 
				    * ((right_lowh_y - right_upch_y) 
					   / (dist_right_upsu**2)) )
				, coords_decimals)

dist_left_upsu = math.sqrt((left_upch_x - left_lowh_x)**2 
                            + (left_upch_y - left_lowh_y)**2)

d_left_upsu = (0.25 * 
               math.sqrt(
			          (dist_left_upsu + midlink + uplink)
					  *
					  (dist_left_upsu + midlink - uplink)
					  *
					  (dist_left_upsu - midlink + uplink)
					  *
					  (-dist_left_upsu + midlink + uplink)
					  )
			    )          #Partial Derivative

left_upwh_x = round(
                  ((left_lowh_x + left_upch_x) / 2) 
				  + 
				  (  ((left_upch_x - left_lowh_x)*(midlink**2 - uplink**2))
				    /
				     (2*(dist_left_upsu**2))  ) 
				  + (2 * d_left_upsu 
				    * ((left_lowh_y - left_upch_y) 
					   / (dist_left_upsu**2)) )
				, coords_decimals)

right_upwh_y = round(
                  ((right_lowh_y + right_upch_y)/2) 
				  + (((right_upch_y - right_lowh_y) * 
					 (midlink**2 - uplink**2)) 
					  / (2*(dist_right_upsu**2))) 
				  + (2 * d_right_upsu * 
					    ((right_lowh_x - right_upch_x)
						/
						(dist_right_upsu**2))
					 )
				, coords_decimals)
				
left_upwh_y = round(
                  ((left_lowh_y + left_upch_y)/2) 
				  + (((left_upch_y - left_lowh_y) * 
					 (midlink**2 - uplink**2)) 
					  / (2*(dist_left_upsu**2))) 
				  - (2 * d_left_upsu * 
					    ((left_lowh_x - left_upch_x)
						/
						(dist_left_upsu**2))
					 )
				, coords_decimals)
				

print("--------ROTATED BODY COORDS----------")
if roll_degrees >= 0:
	print("Degrees: %sdeg CCW" % abs(roll_degrees))
if roll_degrees < 0:
	print("Degrees: %sdeg CW" % abs(roll_degrees))
print("Upper Chassis: (%s, %s), (%s, %s)" % (left_upch_x, left_upch_y, right_upch_x, right_upch_y))
print("Upper Wheel: (%s, %s), (%s, %s)" % (left_upwh_x, left_upwh_y, right_upwh_x, right_upwh_y))
print("Lower Chassis: (%s, %s), (%s, %s)" % (left_loch_x, left_loch_y, right_loch_x, right_loch_y))
print("Lower Wheel: (%s, %s), (%s, %s)" % (left_lowh_x, left_lowh_y, right_lowh_x, right_lowh_y))
if roll_degrees >= 0:
	print("Laden Side Camber: %sdeg" % round(-math.degrees(math.atan((left_upwh_x - left_lowh_x) / (left_upwh_y - left_lowh_y))), 3))
	print("Non-Laden Side Camber: %sdeg" % round(math.degrees(math.atan((right_upwh_x - right_lowh_x) / (right_upwh_y - right_lowh_y))), 3))
if roll_degrees < 0:
	print("Laden Side Camber: %sdeg" % round(math.degrees(math.atan((right_upwh_x - right_lowh_x) / (right_upwh_y - right_lowh_y))), 3))
	print("Non-Laden Side Camber: %sdeg" % round(-math.degrees(math.atan((left_upwh_x - left_lowh_x) / (left_upwh_y - left_lowh_y))), 3))
print("-------------------------------------")



#---------------Tkinter--------------
tick = 1/60
rotspeed = 1/300
sf = 12           #Scale Factor
orx = orx = windowsize_x / 2
ory = windowsize_y / 2 + 150    # Minus Offset (ex. + 150 is 150 down)

line_orx = canvas.create_line(0, ory, windowsize_x, ory)    #X Axis
line_ory = canvas.create_line(orx, 0, orx, windowsize_y)    #Y Axis

chassis_poly = canvas.create_polygon(
                                     orx+sf*left_upch_x, 
									 ory-sf*left_upch_y, 
									 
									 orx+sf*right_upch_x, 
									 ory-sf*right_upch_y, 
									 
									 orx+sf*right_loch_x, 
									 ory-sf*right_loch_y, 
									 
									 orx+sf*left_loch_x, 
									 ory-sf*left_loch_y, 
									 fill='white', outline='black')

if guidelines == True:
	left_hub_guide = canvas.create_oval(
	                                    orx+sf*left_lowh_x + sf*midlink, 
										ory-sf*left_lowh_y + sf*midlink, 
										orx+sf*left_lowh_x - sf*midlink, 
										ory-sf*left_lowh_y - sf*midlink, 
										outline='grey')
	right_hub_guide = canvas.create_oval(
	                                     orx+sf*right_lowh_x + sf*midlink, 
										 ory-sf*right_lowh_y + sf*midlink, 
										 orx+sf*right_lowh_x - sf*midlink, 
										 ory-sf*right_lowh_y - sf*midlink, 
										 outline='grey')
	left_camber_vertical = canvas.create_line(
	                                          orx+sf*left_lowh_x, 
											  0, 
											  orx+sf*left_lowh_x, 
											  windowsize_y, 
											  fill='gray')
	#left_camber_hub = canvas.create_line(orx+sf*left_lowh_x, ory-sf*left_lowh_y, orx+sf*left_upwh_x, ory-sf*left_upwh_y, fill='blue')
	
	left_hub = canvas.create_line(
	                              orx+sf*left_lowh_x, 
								  ory-sf*left_lowh_y, 
								  orx+sf*left_upwh_x, 
								  ory-sf*left_upwh_y, 
								  fill='blue')
	right_camber_vertical = canvas.create_line(
	                                           orx+sf*right_lowh_x, 
											   0, 
											   orx+sf*right_lowh_x, 
											   windowsize_y, 
											   fill='gray')
	right_hub = canvas.create_line(
	                               orx+sf*right_lowh_x, 
								   ory-sf*right_lowh_y, 
								   orx+sf*right_upwh_x, 
								   ory-sf*right_upwh_y, 
								   fill='blue')

up_link_L = canvas.create_line(
                               orx+sf*left_upch_x, 
							   ory - sf*left_upch_y, 
							   orx+sf*left_upwh_x, 
							   ory-sf*left_upwh_y)
lo_link_L = canvas.create_line(
                               orx+sf*left_loch_x, 
							   ory - sf*left_loch_y, 
							   orx+sf*left_lowh_x, 
							   ory-sf*left_lowh_y)

up_link_R = canvas.create_line(
                               orx+sf*right_upch_x, 
							   ory - sf*right_upch_y, 
							   orx+sf*right_upwh_x, 
							   ory-sf*right_upwh_y)
							   
lo_link_R = canvas.create_line(
                               orx+sf*right_loch_x, 
							   ory - sf*right_loch_y, 
							   orx+sf*right_lowh_x, 
							   ory-sf*right_lowh_y)

guide_circle_rad = 4
roll_center_guide = canvas.create_oval(
                                       orx+guide_circle_rad, 
									   ory+guide_circle_rad-sf*roll_center_y, 
									   orx-guide_circle_rad, 
									   ory-guide_circle_rad-sf*roll_center_y, 
									   outline='red')

test_A = 0
test_B = right_upch_xsta
test_C = roll_center_y
test_D = right_upch_ysta
test_guide_rad = math.sqrt(
                           (test_A - test_B)**2 
						   + (test_C - test_D)**2
						   )
						   
test_guide = canvas.create_oval(
                                orx+sf*test_guide_rad, 
								ory+sf*test_guide_rad-sf*roll_center_y, 
								orx-sf*test_guide_rad, 
								ory-sf*test_guide_rad-sf*roll_center_y, 
								outline='red')



#----------Animation Loop------------
loctime = 0         #Start at 0sec
roll_radiansA = 0   #Start at 0rad

while loctime <= 100/tick:
	left_loch_xA = round(left_loch_xsta * math.cos(roll_radiansA)
						- (left_loch_ysta - roll_center_y) * math.sin(roll_radiansA)
						, coords_decimals)

	right_loch_xA = round(right_loch_xsta * math.cos(roll_radiansA)
						- (right_loch_ysta - roll_center_y) * math.sin(roll_radiansA)
						, coords_decimals)

	left_loch_yA = round((left_loch_ysta - roll_center_y) * math.cos(roll_radiansA)
						+ (left_loch_xsta) * math.sin(roll_radiansA)
						+ roll_center_y
						, coords_decimals)

	right_loch_yA = round((right_loch_ysta - roll_center_y) * math.cos(roll_radiansA)
						+ (right_loch_xsta) * math.sin(roll_radiansA)
						+ roll_center_y
						, coords_decimals)

	left_upch_xA = round(left_upch_xsta * math.cos(roll_radiansA)
						- (left_upch_ysta - roll_center_y) * math.sin(roll_radiansA)
						, coords_decimals)

	right_upch_xA = round(right_upch_xsta * math.cos(roll_radiansA)
						- (right_upch_ysta - roll_center_y) * math.sin(roll_radiansA)
						, coords_decimals)

	left_upch_yA = round((left_upch_ysta - roll_center_y) * math.cos(roll_radiansA)
						+ (left_upch_xsta) * math.sin(roll_radiansA)
						+ roll_center_y
						, coords_decimals)

	right_upch_yA = round((right_upch_ysta - roll_center_y) * math.cos(roll_radiansA)
						+ (right_upch_xsta) * math.sin(roll_radiansA)
						+ roll_center_y
						, coords_decimals)
						
	canvas.coords(chassis_poly, 
	              orx+sf*left_upch_xA, 
				  ory-sf*left_upch_yA, 
				  orx+sf*right_upch_xA, 
				  ory-sf*right_upch_yA, 
				  orx+sf*right_loch_xA, 
				  ory-sf*right_loch_yA, 
				  orx+sf*left_loch_xA, 
				  ory-sf*left_loch_yA)
	#STARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
	d_right_losuA = ((lolink**2)                    #Partial Derivatives for circle intersection
					- (right_loch_yA - lowh_y)**2) 
	d_left_losuA = ((lolink**2) 
					- (left_loch_yA - lowh_y)**2)

	right_lowh_xA = round(right_loch_xA 
						+ math.sqrt(d_right_losuA)
						, coords_decimals) #x1

	left_lowh_xA = round(left_loch_xA 
					   - math.sqrt(d_left_losuA)
					   , coords_decimals) #x2
					   
	left_lowh_yA = round(left_lowh_ysta, coords_decimals)
	right_lowh_yA = round(right_lowh_ysta, coords_decimals)      #Wheel y's don't change unless tire itself compresses


	dist_right_upsuA = math.sqrt((right_upch_xA - right_lowh_xA)**2 
								+ (right_upch_yA - right_lowh_yA)**2)

	d_right_upsuA = (0.25 * 
				   math.sqrt(
						  (dist_right_upsuA + midlink + uplink)
						  *
						  (dist_right_upsuA + midlink - uplink)
						  *
						  (dist_right_upsuA - midlink + uplink)
						  *
						  (-dist_right_upsuA + midlink + uplink)
						  )
					)          #Partial Derivative

	right_upwh_xA = round(
					  ((right_lowh_xA + right_upch_xA) / 2) 
					  + 
					  (  ((right_upch_xA - right_lowh_xA)*(midlink**2 - uplink**2))
						/
						 (2*(dist_right_upsuA**2))  ) 
					  - (2 * d_right_upsuA 
						* ((right_lowh_yA - right_upch_yA) 
						   / (dist_right_upsuA**2)) )
					, coords_decimals)

	dist_left_upsuA = math.sqrt((left_upch_xA - left_lowh_xA)**2 
								+ (left_upch_yA - left_lowh_yA)**2)

	d_left_upsuA = (0.25 * 
				   math.sqrt(
						  (dist_left_upsuA + midlink + uplink)
						  *
						  (dist_left_upsuA + midlink - uplink)
						  *
						  (dist_left_upsuA - midlink + uplink)
						  *
						  (-dist_left_upsuA + midlink + uplink)
						  )
					)          #Partial Derivative

	left_upwh_xA = round(
					  ((left_lowh_xA + left_upch_xA) / 2) 
					  + 
					  (  ((left_upch_xA - left_lowh_xA)*(midlink**2 - uplink**2))
						/
						 (2*(dist_left_upsuA**2))  ) 
					  + (2 * d_left_upsuA 
						* ((left_lowh_yA - left_upch_yA) 
						   / (dist_left_upsuA**2)) )
					, coords_decimals)

	right_upwh_yA = round(
					  ((right_lowh_yA + right_upch_yA)/2) 
					  + (((right_upch_yA - right_lowh_yA) * 
						 (midlink**2 - uplink**2)) 
						  / (2*(dist_right_upsuA**2))) 
					  + (2 * d_right_upsuA * 
							((right_lowh_xA - right_upch_xA)
							/
							(dist_right_upsuA**2))
						 )
					, coords_decimals)
					
	left_upwh_yA = round(
					  ((left_lowh_yA + left_upch_yA)/2) 
					  + (((left_upch_yA - left_lowh_yA) * 
						 (midlink**2 - uplink**2)) 
						  / (2*(dist_left_upsuA**2))) 
					  - (2 * d_left_upsuA * 
							((left_lowh_xA - left_upch_xA)
							/
							(dist_left_upsuA**2))
						 )
					, coords_decimals)
	#ENDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
	canvas.coords(up_link_L, 
				  orx+sf*left_upch_xA, 
				  ory - sf*left_upch_yA, 
				  orx+sf*left_upwh_xA, 
				  ory-sf*left_upwh_yA)
	canvas.coords(lo_link_L, 
	              orx+sf*left_loch_xA, 
				  ory - sf*left_loch_yA, 
				  orx+sf*left_lowh_xA, 
				  ory-sf*left_lowh_yA)
	canvas.coords(up_link_R, 
	              orx+sf*right_upch_xA, 
				  ory - sf*right_upch_yA, 
				  orx+sf*right_upwh_xA, 
				  ory-sf*right_upwh_yA)
	canvas.coords(lo_link_R, 
	              orx+sf*right_loch_xA, 
				  ory - sf*right_loch_yA, 
				  orx+sf*right_lowh_xA, 
				  ory-sf*right_lowh_yA)
	if guidelines == True:
		canvas.coords(left_hub_guide, 
		              orx+sf*left_lowh_xA + sf*midlink, 
					  ory-sf*left_lowh_yA + sf*midlink, 
					  orx+sf*left_lowh_xA - sf*midlink, 
					  ory-sf*left_lowh_yA - sf*midlink)
		canvas.coords(right_hub_guide, 
		              orx+sf*right_lowh_xA + sf*midlink, 
					  ory-sf*right_lowh_yA + sf*midlink, 
					  orx+sf*right_lowh_xA - sf*midlink, 
					  ory-sf*right_lowh_yA - sf*midlink)
		canvas.coords(left_camber_vertical, 
		              orx+sf*left_lowh_xA, 
					  0, 
					  orx+sf*left_lowh_xA, 
					  windowsize_y)
		canvas.coords(left_hub, 
		              orx+sf*left_lowh_xA, 
					  ory-sf*left_lowh_yA, 
					  orx+sf*left_upwh_xA, 
					  ory-sf*left_upwh_yA)
		canvas.coords(right_camber_vertical, 
		              orx+sf*right_lowh_xA, 
					  0, 
					  orx+sf*right_lowh_xA, 
					  windowsize_y)
		canvas.coords(right_hub, 
		              orx+sf*right_lowh_xA, 
					  ory-sf*right_lowh_yA, 
					  orx+sf*right_upwh_xA, 
					  ory-sf*right_upwh_yA)
	
	if roll_radians >=0:
		if roll_radiansA >= roll_radians:
			CCWanimation = True
		if roll_radiansA < 0:
			CCWanimation = False

		if CCWanimation == True:
			roll_radiansA = roll_radiansA - rotspeed
		if CCWanimation == False:
			roll_radiansA = roll_radiansA + rotspeed
		#print(roll_radiansA)
	
	if roll_radians <0:
		if roll_radiansA <= roll_radians:
			CCWanimation = False
		if roll_radiansA > 0:
			CCWanimation = True
		
		if CCWanimation == True:
			roll_radiansA = roll_radiansA - rotspeed
		if CCWanimation == False:
			roll_radiansA = roll_radiansA + rotspeed
			
	loctime = loctime + 1
	tk.update()
	time.sleep(tick)
	