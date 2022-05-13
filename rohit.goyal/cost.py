import numpy as np

def dist(A: tuple, B: tuple) -> float:
	return np.sqrt(np.power(A[0] - B[0], 2) + np.power(A[1] - B[1], 2))

def Phi(S_k: list, T: list, r_c: int) -> int:
    sk = set(S_k)
    for x in S_k:
        sk.remove(x)
        covered = set()
        for node in sk:
            for t in T:
                if dist(node, t) <= r_c:
                    covered.add(t)
        if len(covered) == len(T):  return 1
        sk.add(x)
    return 0

def Cost(S: list, T: list, omega1: float, omega2: float, r_c: int) -> float:
    cost_now = 0
    for a in range(len(S)):
        cost_now += omega1 * len(S[a])
        cost_now += omega2 * Phi(S[a], T, r_c)
    return cost_now