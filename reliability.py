import math
import os
import numpy as np
# import dotenv

# load_dotenv()

# _lambda = os.load_dotenv('LAMBDA')
_lambda = 0.02
r_c = 50

def prob(X, Y):
    return math.pow(_lambda, len(X)) * math.pow(1 - _lambda, len(Y))

def f(Y, T):

    dist = lambda a, b : np.sqrt(np.power(a[0]-b[0], 2) + np.power(a[1]-b[1], 2))
    cnt = 0

    for node in Y:
        for target in T:
            if dist(node, target) >= 50:
                cnt += 1

    return 1 if cnt >= 0 else 0

def Reliability(S, T):
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
        final_res += res

    return final_res
