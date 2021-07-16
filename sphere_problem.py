'''what is this program?
    Assume we have N points on a sphere. points are always pushing each other and they cannot leave surface of the sphere. 
    After some play we will see the points in a state of equilibrium. If N > 3 points form a 3d solid. 
    Interestingly we can have a solid with declaring N.(ofcourse they are specific type of solids)
    I wanted to study those solids. so we have this program which gives scatter plot of points of those solids. 
    '''




import math
import numpy as np
import random
import matplotlib.pyplot as plt
   
   
def magnitude(lst):#takes a list of coordinates. Returns magnitude value of that position vector. 
    return math.sqrt(lst[0]*lst[0]+lst[1]*lst[1]+lst[2]*lst[2])

def normalize(lst):#takes a list of coordinates. Returns a normalized version of it. 
    mag = magnitude(lst)
    return [lst[0]/mag,lst[1]/mag,lst[2]/mag]


def angle_bw(v1,v2): #takes two lists of coordinates of point. Returns angle in degrees
    #Dot product
    dot_product = (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])
    #dodging math domain error. making dot product not to overflow from range [-1,1]
    if dot_product < -1:
        dot_product = -1
    elif dot_product > 1:
        dot_product = 1

    return (math.acos(dot_product))*180/math.pi





def points_on_unit_sphere(N):


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
    condition = True
    while condition:
        #in this loop:
        #for a point we find all vectors looking at the point. 
        #Add them and normalize resultant vector. 
        #Make that resultant unit vector as positional vector of the point.
        max_jump_distance = 0
        for i in range(N):
            for j in range(N):
                if rectangular[i] == rectangular[j]:
                    continue
                sub_holder = normalize([rectangular[i][0]-rectangular[j][0],rectangular[i][1]-rectangular[j][1],rectangular[i][2]-rectangular[j][2]])
                force_vector = [force_vector[0]+sub_holder[0],force_vector[1]+sub_holder[1],force_vector[2]+sub_holder[2]]
            force_vector = normalize(force_vector)
            #here we make sure if points are stabalized or not
            jump_distance = magnitude([force_vector[0]-rectangular[i][0],force_vector[1]-rectangular[i][1],force_vector[2]-rectangular[i][2]])
            if jump_distance > max_jump_distance:
                max_jump_distance = jump_distance
            rectangular[i] = force_vector
            force_vector = [0,0,0]
        if max_jump_distance < 0.0000000001:
            condition = False
    #returning finalized rectangular coordinates to plot them.
    return rectangular


N = int(input("Select number of points from 2 to 20: "))

if N >= 2 and N <= 20:#two points are minimum to see action.
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
    print("Number of points should be an integer in range of [2,20]")
