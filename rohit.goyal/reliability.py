import math
import numpy as np

_lambda = 0.02
r_c = 50

def prob(X: list, Y: list) -> float:
    return math.pow(_lambda, len(X)) * math.pow(1 - _lambda, len(Y))

def f(Y: list, T: list) -> int:

    dist = lambda a, b : np.sqrt(np.power(a[0]-b[0], 2) + np.power(a[1]-b[1], 2))
    cnt = 0

    # print('Y:', Y, 'T:', T)

    for node in Y:
        for target in T:
            if dist(node, target) >= r_c:
                cnt += 1

    return 1 if cnt >= 0 else 0

def Reliability(S: list, T: list) -> float:
    n = len(S)
    final_res = 0
    
    for ind in range(1 << n):
        X = []
        Y = []
        
        for i in range(n):
            if ind & (1 << i):
                X.append(S[i])
            else:
                Y.append(S[i])
        # print("X = ", X, "Y = ", Y)
        res = prob(X, Y)
        res *= f(Y, T)
        final_res += res / 4.5

    return final_res

def Reliability_Super(S: list, T:list) -> float:
    relia = 1
    mul = 1
    for k in range(len(S)):
        mul *= abs(1 - Reliability(S[k], T))
    relia -= mul
    return relia