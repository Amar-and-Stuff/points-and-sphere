import math
import numpy as np
import random
from operator import add, sub

def normalize(lst):
    sqr_sum=0
    for i in lst:
        sqr_sum += i*i


    magnitude = math.sqrt(sqr_sum)

    nrm_lst = []

    for i in lst:
        nrm_lst.append(i/magnitude)

    return nrm_lst

def angle_bw(v1,v2):
    return (math.acos((v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])))*180/math.pi



N = int(input("enter number of points: "))
condition = int(input("conditionn:"))


def points_on_unit_sphere(N,condition=50):
    x_ = np.arange(1,11,10/N)
    y_ = np.arange(11,21,10/N)
    z_ = np.arange(21,31,10/N)

    x = list()
    y = list()
    z = list()


    for i in x_:
        x.append(i)
    for i in y_:
        y.append(i)
    for i in z_:
        z.append(i)


    random.shuffle(x)
    random.shuffle(y)
    random.shuffle(z)


    rectangular = list()


    for i in range(N):
        rectangular.append(normalize([x[i],y[i],z[i]]))


    force_vector = [0,0,0]


    while condition:
        for i in range(N):
            for j in range(N):
                if rectangular[i] == rectangular[j]:
                    continue
                force_vector = list(map(add,force_vector,normalize(list(map(sub,rectangular[i],rectangular[j])))))
            force_vector = normalize(force_vector)
            rectangular[i] = force_vector
            force_vector = [0,0,0]
        condition -= 1
    for i in rectangular:
        for j in rectangular:
            print(angle_bw(j,i))
    return rectangular

if N >= 2:

    print(points_on_unit_sphere(N))
else:
    print("mad or wht")
