#!/usr/bin/env python
# coding: utf-8

def polar(x,y,z):
    import numpy as np
    
    r = np.sqrt((x*x)+(y*y)+(z*z))

    if x<0 and y>=0:
        teta = np.degrees(np.arctan(y/x)+np.pi)
    elif x>0:
        teta = np.degrees(np.arctan(y/x))
    elif x<0 and y<0:
        teta = np.degrees(np.arctan(y/x)-np.pi)
    elif x==0 and y>0:
        teta = np.degrees(np.pi/2)
    elif x==0 and y<0:
        teta = np.degrees(-np.pi/2)
    elif x==0 and y==0:
        teta = 0

    if z>0:
        zeta = np.degrees(np.arctan((np.sqrt((x*x)+(y*y))/2)))
    elif z>0:
        zeta = np.degrees(np.arctan((np.sqrt((x*x)+(y*y))/2))+np.pi)
    elif z==0:
        zeta = np.degrees(np.pi/2)
    
    return(r,teta,zeta)

def similarity(filename):
    import numpy as np
    with open(filename) as f:
        lines = f.readlines()
        natoms=int(lines[0])
        frame=np.zeros((natoms,3,1))
        coordinates=np.zeros((natoms,3,1))
        count=2 #if number of atom and title are present
        f=0
        while count < len(lines):
            frame[f,0] = float(lines[count].split()[1])
            frame[f,1] = float(lines[count].split()[2])
            frame[f,2] = float(lines[count].split()[3])
            count+=1
            f+=1
            if count%(natoms+2)==0:
                coordinates=np.append(coordinates,frame,axis=2)
                count+=2
                f=0
        coordinates=np.delete(coordinates,0,axis=2)
        sim=[]
        polaris= np.zeros((natoms,3,len(coordinates[0,0,:])))
        for i in range(0,natoms):
            for j in range(len(coordinates[0,0,:])):
                polaris[i,:,j]=polar(coordinates[i,0,j],coordinates[i,1,j],coordinates[i,2,j])
            for j in range(len(coordinates[0,0,:])):
                for k in range(len(coordinates[0,0,:])):
                    if (polaris[i,:,j]-polaris[i,:,k])[1]==180.0:
                        if (j,k) not in sim and (k,j) not in sim:
                            sim.append((j,k))
                            print("Similarity is detected in between {}".format((j+1,k+1)))
        print("Total similar structure : {}".format(len(sim)))
