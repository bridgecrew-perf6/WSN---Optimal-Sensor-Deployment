from cmath import inf
import numpy as np
from TourConstruction import Tour_Construction
from LocalSearch import LocalSearch
from cost import Cost
from reliability import Reliability

tau_mat = []

def Update_Phermones(D: list, S: list, rho: float, C_ib: float) -> None:
	S = set(S)
	for i in range(len(D)):
		for j in range(len(D)):
			tau_mat[i][j] = (1 - rho) * tau_mat[i][j]
			if D[j] in S:
				tau_mat[i][j] += 1 / C_ib


def Fix_Phermones_MMAS(N: int, rho: float, C_bs: float, b: float) -> None:
	tau_max = 1 / (rho * C_bs)
	tau_min = tau_max / b
	for i in range(N):
		for j in range(N):
			if tau_mat[i][j] > tau_max:
				tau_mat[i][j] = tau_max
			if tau_mat[i][j] < tau_min:
				tau_mat[i][j] = tau_min

def AntColonyOptimization(D: list, T: list, d_o: tuple, R_min: float, _lambda: float,
				N_UB: int, r_s: int, r_c: int, m: int, rho: float, it_max: int, it_c: int) -> tuple:
	
	'''
	D: list of deployable points
	T: list of target points
	d_o: sink node
	R_min: minimum reliability required
	_lambda: probability fraction of node faliure
	N_UB: upper bound of a node coverage (how many sensors should cover a single target point)
	r_s:
	r_c: range od sensor node
	m: number of ants
	rho: phermone evaporation rate
	it_max: maximum iterations
	it_c: maximum iterations with same cost value
	b: min phermone value parameter
	'''

	it = 0
	C_bs = inf
	S_bs = []
	tau_mat = [[1 for i in range(len(D))] for j in range(len(D))]
	it_cc = it_c

	while it < it_max and it_cc > 0:
		
		it += 1
		C_ib = inf
		S_ib = []
		best_ants = []

		for a in range(m):
			S_a = Tour_Construction(D, T, d_o, R_min, tau_mat)
			C_Sa = Cost(S_a, T, 1.2, 3, r_c)
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

		Fix_Phermones_MMAS(len(D), rho, C_bs, b)

	return S_bs, C_bs