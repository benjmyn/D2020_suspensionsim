
import math

#-----------------------
#
#	CHASSIS PARAMETERS
#
#-----------------------

significant_digits = 4 #Decimal places

ct_x = 16 #Chassis-side Top
ct_y = 14 

wt_x = 32 #Wheel-side Top
wt_y = 15

cb_x = 12 #Chassis-side Bottom
cb_y = 6

wb_x = 32 #Wheel-side Bottom
wb_y = 5

hub_link_size = math.sqrt((wt_x-wb_x)**2+(wt_y-wb_y)**2)

tp_x = 32 #Wheel Patch

travel = 2 #2 inches droop

link_top = math.sqrt((wt_y-ct_y)**2+(wt_x-ct_x)**2) #Length of top linkage
link_bottom = math.sqrt((wb_y-cb_y)**2+(wb_x-cb_x)**2) #Length of bottom linkage

print("Link top is %s" % round(link_top, significant_digits-1))
print("Link bottom is %s" % round(link_bottom, significant_digits-1))

wb__y = wb_y + travel #Wheel-side Bottom (y) after Travel
wb__x = math.sqrt((link_bottom)**2 - (wb__y-cb_y)**2)+cb_x #Wheel-side Bottom (x) after Travel

print("New wby is %s" % round(wb__y, significant_digits))
print("New wbx is %s" % round(wb__x, significant_digits))

#Line A
m_top = (wt_y-ct_y) / (wt_x-ct_x)
#m_top * x + (wt_y - (wt_x * m_top))

#Line B
m_bottom = (wb_y - cb_y) / (wb_x - cb_x)
#m_bottom * x + (wb_y - (wb_x * m_bottom))

#Instant Center
ic_x = ((wb_y - (wb_x * m_bottom)) - (wt_y - (wt_x * m_top))) / (m_top-m_bottom)
print("The instant center x is %s" % round(ic_x, significant_digits))
ic_y = m_top * ic_x + (wt_y - (wt_x * m_top))
print("The instant center y is %s" % round(ic_y, significant_digits))

#Roll Center
rc_y = ic_y - ic_x*(-ic_y/(tp_x-ic_x))
print("The roll center height is %s" % round(rc_y, significant_digits))



