#!/usr/bin/env python
# coding: utf-8

import numpy as np

def degree_node(filename):
    with open(filename) as f:
        dat = f.readlines()[3:]
        atom = dat[0].split()
        bond = int(atom[1])
        index = int(atom[0])
        values = np.zeros((index, index),dtype=int)
        dic={}
        connect = dat[index+1:index+1+bond]
        for j, k in enumerate(dat[1:index+1],0):
            dic[j]=[k.split()[3]]
        for i, line in enumerate(connect,0):
            a = int(line.split()[0])
            b = int(line.split()[1])
            c = int(line.split()[2])
            values[a-1][b-1]=c
            values[b-1][a-1]=c
        column_names=range(1,index+1)
        row_names=range(1,index+1)
    return dic,values


def get_values_matrix(filename):
    dic,values=degree_node(filename)
    data=np.sum(values!=0, axis=0)
    for i in list(dic):
        dic[i].append(list(np.where(values[i]>0)[0]))
    return dic, data

def morgan(filename, iteration=0):
    dic, data = get_values_matrix(filename)
    result = data.copy()
    for l in range(1,iteration+1):
        for i in list(dic):
            r = [data[j] for j in dic[i][1]]
            result[i] = sum(r)
        data = result.copy()
    morgan={}
    count=2
    arg= list(data.argsort()[::-1])
    morgan[1]=arg[0]
    while count<len(arg):
        for i in list(morgan.values()):
            for j in arg:
                if j in dic[i][1] and j not in morgan.values():
                    morgan[count]=j
                    count +=1
    return morgan,dic,data


def ring_perception(filename):
    dic,ring=degree_node(filename)
    dic2, data=get_values_matrix(filename)
    temp = []
    while not np.array_equal(temp, data):
        temp = data.copy()
        ring = np.delete(ring, np.where(data==1), axis=0)
        ring = np.delete(ring, np.where(data==1), axis=1)
        data = np.sum(ring!=0, axis=0)
        if np.array_equal(temp, data):
            break
    if 2 in data and data.size>0:
        return print("There is ring structure in {}".format(filename))


    else:
        return print("There is no ring structure in {}".format(filename))

def main():
    morgan, dic, data = morgan("./files/ChEBI_17895.mol", 20)
    print("Morgan for ChEBI_17895.mol \n {}".format(morgan))
    print("----------------------")

    dic,values=degree_node("./files/ChEBI_17895.mol")
    print("Degree Node for ChEBI_17895.mol \n {}".format(values))
    print("----------------------")

    ring_perception("./files/ChEBI_17895.mol")
