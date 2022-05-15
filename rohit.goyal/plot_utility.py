import seaborn as sns
import matplotlib.pyplot as plt

D = [(15, 88), (2, 30), (27, 64), (7, 16), (42, 43), (72, 13), (12, 39), (9, 78), (25, 18), (89, 25)]
T = [(54, 67), (10, 43), (1, 68), (63, 61), (10, 83)]
d_o =  (89, 25)
connected_cover = [[(27, 64), (89, 25), (25, 18), (72, 13), (42, 43)]]

def plot_util(D: list, T: list, d_o: tuple, connected_cover: list = None) -> None:

    if connected_cover is None:
        fig, ax = plt.subplots(figsize=(8,8))
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
        fig, ax = plt.subplots(figsize=(8,8))
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
                    plt.plot(x[0], x[1], 'b.', label='Unsed Deployable Point')
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

        test = True
        for x in connected_cover[0]:
            if x != d_o:
                if test:
                    plt.plot(x[0], x[1], 'bo', label='Deployed Point')
                    test = False
                else:
                    plt.plot(x[0], x[1], 'bo')
            circ = plt.Circle(x, 50, alpha=0.45, edgecolor='b')
            ax.add_artist(circ)

        ax.set_title('Connected cover, covering all target points')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()

plot_util(D, T, d_o)