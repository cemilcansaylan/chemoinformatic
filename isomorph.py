#!/usr/bin/env python
# coding: utf-8

def isomorph(filename, atom1=None, atom2=None, random=False):
    import numpy as np
    import math
    from random import randint
    with open(filename) as f:
        dat = f.readlines()[3:]
        atom = dat[0].split()
        bond = int(atom[1])
        index = int(atom[0])
        print("{} isomorphic structures with H".format(math.factorial(index)))
        dic={}
        hyd=[]
        connect = dat[index+1:index+1+bond]
        for j, k in enumerate(dat[1:index+1],0):
            dic[j]=[k.split()[3]]
            if k.split()[3]=='H':
                hyd.append(j+1)
            values = np.zeros((index-len(hyd), index-len(hyd)),dtype=int)
        print("{} isomorphic structures w/o H".format(math.factorial(index-len(hyd))))
        for i, line in enumerate(connect,0):
            a = int(line.split()[0])
            b = int(line.split()[1])
            c = int(line.split()[2])
            if a and b not in hyd:
                values[a-1][b-1]=c
                values[b-1][a-1]=c
        try:
            if atom1 and atom2 is not None:
                values[:,[atom1, atom2]] = values[:,[atom2, atom1]]
                values[[atom1, atom2],:] = values[[atom2, atom1],:]
        except:
            if random is True:
                r1= randint(0, index-len(hyd)-1)
                r2= randint(0, index-len(hyd)-1)
                values[:,[r1, r2]] = values[:,[r2, r1]]
                values[[r1, r2],:] = values[[r2, r1],:]
    return values


