import matplotlib.pyplot as plt
import numpy as np
import time

def try_matplotlib():

    fig = plt.figure()

    plt.plot([1,3,4],[2,1,6])
    plt.show()
    
    fig.savefig('output.png', dpi=fig.dpi)

    return