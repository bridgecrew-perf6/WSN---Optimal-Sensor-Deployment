import numpy as np
from reliability import Reliability

# D = input("Enter all the deployable points: ")
# T = input("Enter all the target points: ")
# d_o = input("Position of HeadQuarter/Sink Node: ")
# _lambda = float(input('Probablity fraction of Node faliure(0, 1): '))
# R_min = float(input('Minimum Reliability Required: '))
# N_ub = int(input('Minimum number of node to cover a target: '))
# rs = int(input('Range of '))
# rc = int(input('Range of Sensor Node: '))

D = [(30, 20), (19, 11), (83, 18), (4, 33), (14, 40), (59, 46), (77, 21), (76, 42), (46, 5), (27, 90), (40, 61), (23, 8), (69, 9), (31, 41), (71, 29), (93, 11), (40, 67), (52, 31), (17, 52), (46, 16), (78, 66), (88, 70), (22, 89), (70, 18), (56, 96), (16, 46), (43, 85), (65, 64), (79, 97), (94, 62), (43, 30), (89, 57), (17, 83), (16, 91), (44, 57), (28, 2), (40, 96), (12, 16), (74, 41), (22, 7), (48, 22), (37, 36), (20, 24), (88, 16), (18,  75), (83, 76), (43, 58), (10, 31), (91, 96), (21, 35), (12, 82), (80, 19), (15, 93), (79, 21), (21, 13), (72, 57), (65, 45), (22, 24), (2, 37), (78, 9)]
T = [(8, 72), (52, 57), (77, 63), (56, 85), (11, 95), (11, 6), (69, 15), (84, 88), (75, 45), (34, 41), (94, 21), (42, 71), (3, 2), (43, 36), (34, 47), (100, 63), (55, 52), (34, 40), (55, 92), (20, 25)]
d_o = (19, 11)
_lambda = 0.02
R_min = 0.99
rc = 50

def fix_point(P: str) -> tuple:
	P = P.rstrip(')').lstrip('(')
	P = tuple(map(int, P.split(',')))
	return P

def fix_array(X: str) -> list:
	X = X.replace(' ', '')
	X = X.rstrip(']').lstrip('[')
	X = list(X.split('),'))
	ret = []
	for val in X:
		ret.append(fix_point(val))
	return ret

def equal(T_cov: list, T: list) -> bool:
    for item in T:
        if item not in T_cov:
            return False
    return True

def dist(A: tuple, B: tuple) -> float:
	return np.sqrt(np.power(A[0] - B[0], 2) + np.power(A[1] - B[1], 2))

def find_coverage_gains(N: list, T: list, T_cov: list) -> list:
	T_cov = set(T_cov)
	ret = []
	for p in N:
		cnt = 0
		for t in T:
			if t not in T_cov and dist(t, p) <= rc:
				cnt += 1
		ret.append(cnt)
	return ret

# D = fix_array(D)
# T = fix_array(T)
# d_o = fix_point(d_o)

S = []
R = 0
k = 0
D_minus = D.copy()
D_minus.remove(d_o)

while R < R_min:
	k = k+1
	S_k = [d_o]
	T_cov = []
	for t in T:
		if dist(d_o, t) <= rc:
			T_cov.append(t)
	while not equal(T_cov, T):
		# print(T_cov, '\n', T, '\n', equal(T_cov, T))
		# print(D_minus)
		if len(S_k) == 0:
			N_next = {p for p in D_minus if dist(p, d_o) <= rc}
		else:
			N_next = {p for p in D_minus for d in S_k if dist(p, d) <= rc}
		N_next = N_next - set(S_k)
		N_next = list(N_next)
		# print('N_next =', N_next)
		coverage_gain = find_coverage_gains(N_next, T, T_cov)
		# print('C gain =', coverage_gain)
		g_max = max(coverage_gain)
		for i in range(len(coverage_gain)):
			if coverage_gain[i] == g_max:
				S_k.append(N_next[i])
				for t in T:
					if not t in T_cov and dist(t, N_next[i]) <= rc:
						T_cov.append(t)
	S.append(S_k)
	R += Reliability(S_k, T)
	 

print("Connected Covers:", S)
