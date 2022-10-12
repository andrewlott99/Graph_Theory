
import itertools
import numpy as np
import math
from sympy import factorint
from math import factorial as fact

K_4 = {1: {2,3,4}, 2:{1,3,4}, 3:{1,2,4}, 4:{1,2,3}}

K_10 = {1: {2,3,4,5,6,7,8,9,10}, 2: {1,3,4,5,6,7,8,9,10}, 3:{1,2,4,5,6,7,8,9,10}, 4:{1,2,3,5,6,7,8,9,10}, 5:{1,2,3,4,6,7,8,9,10}, 6:{1,2,3,4,5,7,8,9,10}, 7:{1,2,3,4,5,6,8,9,10}, 8:{1,2,3,4,5,6,7,9,10}, 9:{1,2,3,4,5,6,7,8,10}, 10:{1,2,3,4,5,6,7,8,9}}

K_44 = {1: {3,4}, 2:{3,4}, 3:{1,2}, 4:{1,2}}




def check_if_independent(G):
	for v in G.keys():
		for u in G.keys():
			if u in G[v]:
				return False

	return True




def generate_partitions(G):
	partition_list = []

	v = list(G.keys())[0]
	v_neighborhood = G[v]
	if len(G.keys())==1:
		part_1 = {}
		part_2 = {}
		part_1[v]=G[v]
		partition_list = partition_list + [[part_1,part_2]]
		return partition_list


	del G[v]



	for partition in generate_partitions(G):
		part_1 = partition[0]
		part_2 = partition [1]
		part_1_copy = part_1.copy()
		part_2_copy = part_2.copy()

		part_1_copy[v] = v_neighborhood
		partition_list = partition_list + [[part_1_copy, part_2]]

		part_2_copy[v] = v_neighborhood
		partition_list = partition_list + [[part_1, part_2_copy]]

	return partition_list



def check_if_bipartite(G):
	for partition in generate_partitions(G):
		if check_if_independent(partition[0])==True and check_if_independent(partition[1])==True:
			return True
	return False 

print(check_if_bipartite(K_10))





