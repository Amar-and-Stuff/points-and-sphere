import math
import numpy as np
import random
from operator import add, sub
import matplotlib.pyplot as plt
   
   
def normalize(lst):#takes a list of coordinates. Returns a normalized version of it. 
    sqr_sum=0

    for i in lst:
        sqr_sum += i*i

    magnitude = math.sqrt(sqr_sum)
    nrm_lst = []

    for i in lst:
        nrm_lst.append(i/magnitude)

    return nrm_lst


def angle_bw(v1,v2): #takes two lists of coordinates of point. Returns angle in degrees
    #Dot product
    dot_product = (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])
    #dodging math domain error. making dot product not to overflow from range [-1,1]
    if dot_product < -1:
        dot_product = -1
    elif dot_product > 1:
        dot_product = 1

    return (math.acos(dot_product))*180/math.pi





def points_on_unit_sphere(N,condition=100):


    #generating N points from specified range to get unique points
    x = [i for i in np.arange(1,11,10/N)]
    y = [i for i in np.arange(11,21,10/N)]
    z = [i for i in np.arange(21,31,10/N)]

    #shuffling points for randomness
    random.shuffle(x)
    random.shuffle(y)
    random.shuffle(z)

    #making positional vectors in rectangular coordinate geometry
    rectangular = [normalize([x[i],y[i],z[i]]) for i in range(N)]

    #force_vector to find direction of force form all other points
    force_vector = [0,0,0]


    while condition:
        #in this loop:
        #for a point we find all vectors looking at the point. 
        #Add them and normalize resultant vector. 
        #Make that resultant unit vector as positional vector of the point.
        for i in range(N):
            for j in range(N):
                if rectangular[i] == rectangular[j]:
                    continue
                force_vector = list(map(add,force_vector,normalize(list(map(sub,rectangular[i],rectangular[j])))))
            force_vector = normalize(force_vector)
            rectangular[i] = force_vector
            force_vector = [0,0,0]
        condition -= 1

    #returning finalized rectangular coordinates to plot them.
    return rectangular


N = int(input("enter number of points: "))

if N >= 2:#two points are minimum to see action.
    #storing finalized rectangular coordinates in final_points.
    final_points = points_on_unit_sphere(N)

    #distributing coordinates to plot
    x = [i[0] for i in final_points]
    y = [i[1] for i in final_points]
    z = [i[2] for i in final_points]
    ax = plt.axes(projection="3d")
    ax.scatter(x,y,z)
    plt.show()
else:#mad or wht
    print("mad or wht")
