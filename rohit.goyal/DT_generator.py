import random
import sys

from scipy import rand

n_cmd = len(sys.argv)

if n_cmd < 3 or n_cmd > 4:
    print('Missing command line arguments')
    print('python ./DT_generator.py <num_deployable_points> <num_target_points> [optinal <max_grid_position>]')

else:
    try:
        nd = int(sys.argv[1])
        nt = int(sys.argv[2])
        gmax = 100
        if n_cmd == 4:
            gmax = int(sys.argv[3])

        D = []
        T = []

        for i in range(nd):
            D.append((random.randint(1, gmax), random.randint(1, gmax)))

        for i in range(nt):
            T.append((random.randint(1, gmax), random.randint(1, gmax)))

        print('D =', D)
        print('T =', T)
        print('d_o = ', random.choice(D))

    except:
        print('Some error occured while generating points')