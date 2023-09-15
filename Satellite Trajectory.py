import numpy as np
import matplotlib.pyplot as plt
import math

G = 6.67 * 10**-11
M = 5.97 * 10**24
R = 6371 * 10**3

print("Enter desired value of T in Seconds: ")
T = float(input())

h = (G*M*T*T/(4*3.142*3.142))**(1/3) - R
print("Altitude in meters: ", h)

#Calculating number of seconds in the given time intervals
TOnceADay = 86400
T120Minutes = 7200
T30Minutes = 1800

T = TOnceADay
h = (G*M*T*T/(4*3.142*3.142))**(1/3) - R
print("Altitude in meters when Time Period is Once a Day: ", h)

T = T120Minutes
h = (G*M*T*T/(4*3.142*3.142))**(1/3) - R
print("Altitude in meters when Time Period is 120 minutes: ", h)

T = T30Minutes
h = (G*M*T*T/(4*3.142*3.142))**(1/3) - R
print("Altitude in meters when Time Period is 30 minutes: ", h)

# From the last calculation, we get a negative altitude. This means that it is not a feasible Time Period for a
# satellite to remain in orbit. We must have a much higher time period for the altitude to be sufficiently high.


