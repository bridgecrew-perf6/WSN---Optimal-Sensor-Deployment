import matplotlib.pyplot as plt

D = [(30, 20), (19, 11), (83, 18), (4, 33), (14, 40), (59, 46), (77, 21), (76, 42), (46, 5), (27, 90), (40, 61), (23, 8), (69, 9), (31, 41), (71, 29), (93, 11), (40, 67), (52, 31), (17, 52), (46, 16), (78, 66), (88, 70), (22, 89), (70, 18), (56, 96), (16, 46), (43, 85), (65, 64), (79, 97), (94, 62), (43, 30), (89, 57), (17, 83), (16, 91), (44, 57), (28, 2), (40, 96), (12, 16), (74, 41), (22, 7), (48, 22), (37, 36), (20, 24), (88, 16), (18,  75), (83, 76), (43, 58), (10, 31), (91, 96), (21, 35), (12, 82), (80, 19), (15, 93), (79, 21), (21, 13), (72, 57), (65, 45), (22, 24), (2, 37), (78, 9)]
T = [(8, 72), (52, 57), (77, 63), (56, 85), (11, 95), (11, 6), (69, 15), (84, 88), (75, 45), (34, 41), (94, 21), (42, 71), (3, 2), (43, 36), (34, 47), (100, 63), (55, 52), (34, 40), (55, 92), (20, 25)]
d_o = (19, 11)
connected_cover = [[(19, 11), (37, 36), (52, 31), (65, 64), (72, 57), (43, 85), (65, 45), (40, 67), (89, 57), (78, 66), (59, 46)]]

def plot_util(D: list, T: list, d_o: tuple, connected_cover: list = None) -> None:

    if connected_cover is None:
        fig, ax = plt.subplots(figsize=(8.5,6))
        ax.set_xlim((0, 100))
        ax.set_ylim((0, 100))
        for i in range(10, 100, 10):
            plt.plot([0, 100], [i, i], 'k--', alpha=0.5, linewidth=0.5)
            plt.plot([i, i], [0, 100], 'k--', alpha=0.5, linewidth=0.5)

        test = True
        for x in D:
            if test:
                plt.plot(x[0], x[1], 'b.', label='Deployable Point')
                test = False
            else:
                plt.plot(x[0], x[1], 'b.')
        plt.plot(d_o[0], d_o[1], 'b^', label='Sink Node')

        test = True
        for x in T:
            if test:
                plt.plot(x[0], x[1], 'kX', label='Target Point')
                test = False
            else:
                plt.plot(x[0], x[1], 'kX')

        plt.title('All deployable points and target points')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()

    if connected_cover is not None:
        print(connected_cover)
        fig, ax = plt.subplots(figsize=(8.5,6))
        ax.set_xlim((0, 100))
        ax.set_ylim((0, 100))
        # ax.
        for i in range(10, 100, 10):
            plt.plot([0, 100], [i, i], 'k--', alpha=0.5, linewidth=0.5)
            plt.plot([i, i], [0, 100], 'k--', alpha=0.5, linewidth=0.5)

        test = True
        for x in D:
            if x not in connected_cover[0]:
                if test:
                    plt.plot(x[0], x[1], 'r.', label='Unsed Deployable Point')
                    test = False
                else:
                    plt.plot(x[0], x[1], 'r.')
        plt.plot(d_o[0], d_o[1], 'y^', label='Sink Node')

        test = True
        for x in T:
            if test:
                plt.plot(x[0], x[1], 'kX', label='Target Point')
                test = False
            else:
                plt.plot(x[0], x[1], 'kX')

        test = True
        for x in connected_cover[0]:
            if x != d_o:
                if test:
                    plt.plot(x[0], x[1], 'yo', label='Deployed Point')
                    test = False
                else:
                    plt.plot(x[0], x[1], 'yo')
            circ = plt.Circle(x, 50, alpha=0.45, edgecolor='b')
            ax.add_artist(circ)

        ax.set_title('Connected cover, covering all target points')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()

plot_util(D, T, d_o, connected_cover)