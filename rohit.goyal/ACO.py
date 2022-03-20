import numpy as np
import os
from dotenv import load_dotenv
import TourConstruction
import LocalSearch

load_dotenv()

_lambda = os.load_dotenv('LAMBDA')
r_c = os.load_dotenv('NODE_RANGE')

Reliability = TourConstruction.Reliability

def AntColonyOptimization(D, T, d_o, R_min):
    
    S = []
    R_S = 0
    k = 0
    D_minus = D.copy()
    
    while R_S < R_min:
        R_S = Reliability(S)

    return S, R_S