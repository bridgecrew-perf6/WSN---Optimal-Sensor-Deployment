from cost import Phi, dist
from reliability import Reliability_Super
from collections import deque

def LocalSearch(S: list, T: list, C_S: float, R_S: float, R_min: float, d_o: tuple,
            r_c: int, omega1: float = 1.2, omega2: float = 3) -> tuple:
    '''
    S: Set of connected covers
    T: list of target nodes
    C_S: Cost of set S
    R_S: Reliability of set S
    R_min: minimum reliability required
    d_o: sink node
    r_c: range of sensor node
    omega1, omega2: parameters for tuning cost function
    '''

    C_LS = C_S
    S_LS = S.copy()
    R_LS = R_S
    S_temp = S_LS.copy()
    R_temp = R_LS

    for k in range(len(S)):
        if Phi(S[k], T, r_c) == 1:
            s_pk = set(S[k])

            for node in S[k]:
                if node == d_o: continue

                s_pk.remove(node)
                covered = set()

                for t in T:
                    for n in s_pk:
                        if dist(t, n) <= r_c:
                            covered.add(t)

                vis = dict()

                for n in s_pk:  vis[n] = False
                
                vis[d_o] = True
                que = deque([d_o])

                while len(que) > 0:
                    top = que.popleft()
                    for key in vis.keys():
                        if vis[key] == False and dist(key, top) <= r_c:
                            vis[key] = True
                            que.append(key)

                for key, status in vis.items():
                    if not status:
                        s_pk.add(node)
                        break

                if len(covered) != len(T):
                    s_pk.add(node)

            S_temp[k] = list(s_pk)
            R_temp = Reliability_Super(S_temp, T)

            if R_temp >= R_min:
                S_LS = S_temp.copy()
                R_LS = R_temp
                C_LS = C_LS - omega2
            else:
                S_temp = S_LS.copy()
                R_S_temp = R_LS

    return S_LS, C_LS

