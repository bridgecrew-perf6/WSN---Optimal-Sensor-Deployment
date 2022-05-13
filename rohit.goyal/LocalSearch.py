import numpy as np

def LocalSearch(S, C_S, R_S):
    C_LS = C_S
    S_LS = S.copy()
    R_LS = R_S
    S_temp = S_LS.copy()
    R_temp = R_LS
    cost_now = 0
    for i in range(len(S)):
        cost_now += len(S[i])
        