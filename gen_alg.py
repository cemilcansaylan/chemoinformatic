#!/usr/bin/env python
# coding: utf-8

import numpy as np

def _distance_matrix(NUM_OF_GENE):
    dis_mat = np.random.uniform(low=0.0, high=5.0, size=(NUM_OF_GENE, NUM_OF_GENE))
    dis_mat = (dis_mat + dis_mat.T) / 2
    np.fill_diagonal(dis_mat, 0)
    return dis_mat

def _init_pop_mat(POPULATION_SIZE,NUM_OF_GENE):
    matrix = np.zeros((POPULATION_SIZE, NUM_OF_GENE),dtype=int)
    gene_pool = [gene for gene in range(NUM_OF_GENE)]
    for i in range(POPULATION_SIZE):
        np.random.shuffle(gene_pool)
        matrix[i,:]=gene_pool
    return matrix

def _mating_pool(POPULATION_SIZE):
    pool = np.arange(POPULATION_SIZE)
    np.random.shuffle(pool)
    return pool

def _cross_over(ind1,ind2,genes,MATRIX):
    np.random.shuffle(genes)
    genes = genes[:4]
    ind1 = MATRIX[ind1]
    ind2 = MATRIX[ind2]
    temp=ind1[np.where(np.isin(ind1,genes,invert=True))].copy()
    ind1[np.where(np.isin(ind1,genes,invert=True))]=ind2[np.where(np.isin(ind2,genes,invert=True))].copy()
    ind2[np.where(np.isin(ind2,genes,invert=True))]=temp.copy()
    return ind1,ind2

def mutation(ind,NUM_OF_GENE):
    swap_gene = np.random.randint(0,NUM_OF_GENE,2)
    temp = ind[swap_gene[0]]
    ind[swap_gene[0]] = ind[swap_gene[1]]
    ind[swap_gene[1]] = temp

def fit_score(ind1, NUM_OF_GENE, DISTANCE):
    score = 0
    for i, j in zip(range(NUM_OF_GENE - 1), range(1, NUM_OF_GENE)):
        score = score + DISTANCE[ind1[i], ind1[j]]
    return score

def gene_alg(MATRIX, DISTANCE, genes, itaration):
    POPULATION_SIZE=len(MATRIX)
    NUM_OF_GENE=len(genes)
    count = 0
    while count < itaration:
        pool = _mating_pool(POPULATION_SIZE)
        for i, j in zip(range(0, len(pool) - 1, 2), range(1, len(pool), 2)):
            i1, i2 = _cross_over(pool[i], pool[j], genes, MATRIX)
            mutation(i1,NUM_OF_GENE)
            MATRIX=np.vstack([MATRIX,i1])
            MATRIX=np.vstack([MATRIX,i2])
        score = []
        for i in pool:
            score.append([i, fit_score(MATRIX[i], NUM_OF_GENE, DISTANCE)])
        score = sorted(score, key=lambda x: x[1])
        for i in range(len(score)):
            MATRIX[i]=MATRIX[score[i][0]]
        if count == 0:
            min_value = score[0][1]
            min_path = MATRIX[score[0][0]]
        elif score[0][1] < min_value:
            min_value = score[0][1]
            min_path = MATRIX[score[0][0]].copy()
        print(" {} itaration min_value {} and min_path {}".format(count,min_value,min_path))
        MATRIX=np.vsplit(MATRIX,2)[0]
        count += 1 

def main():
    
    genes = np.arange(0,10)
    NUM_OF_GENE=len(genes)
    POPULATION_SIZE=200

    DISTANCE = _distance_matrix(NUM_OF_GENE)
    MATRIX = _init_pop_mat(POPULATION_SIZE, NUM_OF_GENE)

    gene_alg(MATRIX, DISTANCE, genes, itaration=10)

if __name__ == "__main__":
    main()
