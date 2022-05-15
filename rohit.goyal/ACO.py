from cmath import inf
from collections import defaultdict
import numpy as np
from TourConstruction import Tour_Construction
from LocalSearch import LocalSearch
from cost import Cost
from reliability import Reliability_Super
import matplotlib.pyplot as plt
from plot_utility import plot_util

tau_mat = defaultdict(lambda : defaultdict(lambda : 1))

def Update_Phermones(D: list, S: list, rho: float, C_ib: float) -> None:

	global tau_mat

	Good_nodes = set()
	for s in S:
		for node in s:
			Good_nodes.add(node)
	for node1 in D:
		for node2 in D:
			tau_mat[node1][node2] = (1 - rho) * tau_mat[node1][node2]
			if node2 in Good_nodes:
				tau_mat[node1][node2] += 1 / C_ib


def Fix_Phermones_MMAS(N: int, rho: float, C_bs: float, b: float) -> None:

	global tau_mat

	tau_max = 1 / (rho * C_bs)
	tau_min = tau_max / b
	for i in range(N):
		for j in range(N):
			if tau_mat[i][j] > tau_max:
				tau_mat[i][j] = tau_max
			if tau_mat[i][j] < tau_min:
				tau_mat[i][j] = tau_min

def AntColonyOptimization(D: list, T: list, d_o: tuple, R_min: float, _lambda: float,
				N_UB: int, r_c: int, m: int, rho: float, it_max: int,
				it_c: int, b: float = 10, omega1: float = 1.2, omega2: float = 3) -> tuple:
	
	'''
	D: list of deployable points
	T: list of target points
	d_o: sink node
	R_min: minimum reliability required
	_lambda: probability fraction of node faliure
	N_UB: upper bound of a node coverage (how many sensors should cover a single target point)
	r_c: range od sensor node
	m: number of ants
	rho: phermone evaporation rate
	it_max: maximum iterations
	it_c: maximum iterations with same cost value
	b: min phermone value parameter
	'''

	global tau_mat

	cost_array = []

	it = 0
	C_bs = inf
	S_bs = []
	for node1 in D:
		for node2 in D:
			tau_mat[node1][node2] = 1
	it_cc = it_c

	graph_done_tc = False
	tc_graph = []
	ls_graph = []

	while it < it_max and it_cc > 0:
		
		it += 1
		C_ib = inf
		S_ib = []
		best_ants = []

		for a in range(m):
			S_a = Tour_Construction(D, T, d_o, R_min, tau_mat, r_c)
			if not graph_done_tc:
				graph_done_tc = True
				tc_graph = S_a.copy()
			C_Sa = Cost(S_a, T, omega1, omega2, r_c)
			R_Sa = Reliability_Super(S_a, T)
			S_a, C_Sa = LocalSearch(S_a, T, C_Sa, R_Sa, R_min, d_o, r_c)
			ls_graph = S_a.copy()
			if C_Sa < C_ib:
				C_ib, S_ib = C_Sa, S_a.copy()
				best_ants.clear()
				best_ants.append(a)
			elif C_Sa == C_ib:
				best_ants.append(a)
		
		Update_Phermones(D, S_ib, rho, C_ib)

		if C_ib < C_bs:
			S_bs = S_ib.copy()
			C_bs = C_ib
			it_cc = it_c
		else:
			it_cc -= 1

		print(C_bs)
		cost_array.append(C_bs)

		Fix_Phermones_MMAS(len(D), rho, C_bs, b)

	plot_util(D, T, d_o)
	# print(tc_graph, ls_graph)
	plot_util(D, T, d_o, tc_graph)
	plot_util(D, T, d_o, ls_graph)

	plt.figure(figsize=(6,6))
	plt.plot(cost_array)
	plt.xlabel('Inerations')
	plt.ylabel('Cost')
	plt.title('Cost vs Iteration Graph')
	plt.show()
	return S_bs, C_bs