import numpy as np
import os
import TourConstruction
import LocalSearch

_lambda = 0.02
r_c = 50

Reliability = TourConstruction.Reliability

def AntColonyOptimization(D, T, d_o, R_min):
	
	S = []
	R_S = 0
	k = 0
	D_minus = D.copy()
	
	while R_S < R_min:
		k = k+1
		S_k = []
		T_cov = []

		while TourConstruction.equal(T_cov, T):
			
			dist = lambda a, b: np.sqrt(np.square(a[0] - b[0]) + np.square(a[1] - b[1]))
			N_next = []
			
			if len(S_k) == 0:
				for d in D_minus:
					if dist(d, d_o) < r_c:
						N_next.append(d)
			
			else:
				for dd in S_k:
					for d in D_minus:
						if dist(d, dd) < r_c and d not in S_k:
							N_next.append(d)

			

		R_S = Reliability(S)


	return S, R_S