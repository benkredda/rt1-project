from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.68
""" float: Threshold for the control of the orientation"""

silver = True
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

R = Robot()
""" instance of the class Robot"""

j = 0
""" integer: used for repetition of a process"""
def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

while 1:
    if silver == True: # if silver is True, then we look for a silver token, otherwise for a golden one, and we move the robot forward.
	dist, rot_y = find_silver_token()
	drive(10,1)
    else:
	dist, rot_y = find_golden_token()
	drive(10,1)
    if dist==-1: # if no token is detected, we make the robot turn    
        print("I don't see any token!!")
	turn(+10, 1)
    elif dist <d_th: # if we are close to the token, we try grab it.
        print("Found it!")
        if R.grab(): # if we grab the silver token, we turn the robot to the right.
        	print("Gotcha!")
        	turn(10, 2)
	 	silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token which is the golden token.
	  	while silver == False :
			dist, rot_y = find_golden_token() #we want to find the closest golden token inorder to pair them together
			if dist==-1: # if no token is detected, we make the robot turn    
				print("I see no token!!")
				turn(+10, 1)
			elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
				print("Ah, that's what i'll do.")
				drive(10, 0.5)
				print (dist)
				if dist <d_th:
					print("Find it!")
					R.release() #we release the silver token near to the golden one 
					j = j+1 #this equation represents the itteration of the process, it will be repeated six times
					drive(-40,2)
					turn(-15,2)
					silver = not silver
					if j == 6:
						exit() # we exit and break after pairing all the six boxes
					break
			elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
				print("Left a bit...")
				turn(-2, 0.5)
		    	elif rot_y > a_th:
				print("Right a bit...")
				turn(+2, 0.5)
			else :
				print("i'm far a lit bit")
	else:
	    print("Aww, I'm not close enough.")
		    

