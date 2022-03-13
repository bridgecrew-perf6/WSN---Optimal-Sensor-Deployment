from shutil import ReadError
import numpy as np
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

r_c = os.load_dotenv('NODE_RANGE')
alpha = os.load_dotenv('ALPHA')
beta = os.load_dotenv('BETA')
_lambda = os.load_dotenv('LAMBDA')
Target_under = defaultdict(lambda :[])

def equal(T_cov, T):
    for item in T_cov:
        if item not in T:
            return False
    return True

def Reliability(S):
    pass

def find_Target_under(D, T):

    def dist(a, b):
        return np.sqrt(np.power(a, 2)+np.power(b, 2))

    for d in D:
        for t in T:
            if dist(d, t) <= r_c:
                Target_under[d].append(t)


def find_N_ifull(node_st, node_points):
    pass

def find_N_eff(node_st, node_points):
    pass

def find_coverage_gain(N):
    pass

def next_best_node(d_o, tau):
    pass

def Tour_Construction(ant_num, D, T, d_o, R_min, tau_mat):
    '''
        ant_num: number of iterations we are on
        D: set of possible node positions (x, y)
        T: set of target points (x, y)
        d_o: starting point belongs to D
        R_min: min reliability lie in [0, 1]
        _lambda: failure probabilty of node
        tau_mat: phermone value of each path
        r_c: communication range of each node
    '''
    
    # initialization of variables
    S = []
    S_reliability = 0
    k = 0
    D_minus = D.copy()
    find_Target_under(D, T)
    
    #finding a reliable connected cover
    while S_reliability < R_min:
        
        #initializaion variables for this iteration
        k += 1
        S_k, T_cov = [[] for count in range(2)]

        # covering all target points
        while not equal(T_cov, T):
            N_ifull = find_N_ifull(d_o, D_minus)
            N_ieff = find_N_eff(d_o, N_ifull)
            N_i = N_ieff if len(N_ieff) != 0 else N_ifull
            converage_gain_i = find_coverage_gain(N_i)
            S_k.append(d_o)
            for target in Target_under[d_o]:
                if target not in T_cov:
                    T_cov.append(target)
            d_o = next_best_node(d_o, tau_mat)
        
        # Updating the variables after covering all arget points
        S.append(S_k)
        S_reliability += Reliability(S_k)
        for node in S_k:
            D_minus.remove(node)
    
    return S