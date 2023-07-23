import matplotlib.pyplot as plt

def linegraph(line_number = 1, xlim_abosulute_left = None, xlim_abosulute_right = None):
    fig, ax = plt.subplots()
    step = 0
    for i in range(line_number):
        ax.plot([0, step+1],[step, step+1])
        step+=1

    ax.set_xlim(xlim_abosulute_left, xlim_abosulute_right)
    return fig