import matplotlib.pyplot as plt
# from matplotlib.cbook import cbook
import numpy as np

D = [(15, 88), (2, 30), (27, 64), (7, 16), (42, 43), (72, 13), (12, 39), (9, 78), (25, 18), (89, 25)]
T = [(54, 67), (10, 43), (1, 68), (63, 61), (10, 83)]
d_o =  (89, 25)
connected_cover = [[(27, 64), (89, 25), (25, 18), (72, 13), (42, 43)]]

for x in D:
    plt.plot(x[0], x[1], 'g.')

for x in T:
    plt.plot(x[0], x[1], '')
plt.show()