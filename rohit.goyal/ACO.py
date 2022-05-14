from cmath import inf
import numpy as np
from TourConstruction import Tour_Construction
from LocalSearch import LocalSearch
from cost import Cost
from reliability import Reliability

tau_mat = []

def Update_Phermones(S: list, best_ants: list) -> None:
	pass

def AntColonyOptimization(D: list, T: list, d_o: tuple, R_min: float, _lambda: float,
				N_UB: int, r_s: int, r_c: int, m: int, rho, it_max: int, it_c: int) -> tuple:
	
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
	'''

	it = 0
	C_bs = inf
	S_bs = []
	tau_o = 1

	while it < it_max and it_c > 0:
		
		it += 1
		C_ib = inf
		S_ib
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
		
		Update_Phermones(S_ib, best_ants)

