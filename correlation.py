import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import repeat
import pylab
import copy

def gen_signal():

    signal = []
    for x in range(10):
        signal += list(repeat(random.randint(-1,1), 100))

    return np.array(signal)



def cross_correlate(xs, ys, minval=False):
    """Takes two arrays and finds the x-value of the second at which both correlate highest.
        xs and ys are the first and second signals, respectively, with minval being a boolean
        declaring whether or not the x-value of minimum correlation should be found as well."""



    maxcorr = 0
    mincorr = 5
    xmax = 0
    xmin = 0
    for X in range(len(ys) - len(xs)):
        corr = 0
        for x in range(len(xs)):
            corr +=  (xs[x] * ys[x + X])
        if corr > maxcorr:
            maxcorr = corr
            xmax = X
        if minval and corr < mincorr:
            mincorr = corr
            xmin = X

    

    plt.subplot(211)
    plt.plot(xs, color="y")
    plt.ylabel("One-Dimensional Signal Pre-image")
    plt.subplot(212)
    plt.axvline(x=xmax, linewidth=1, color='r')
    if minval:
        plt.axvline(x=xmin, linewidth=1, color='blue')
        plt.text(s=("Min: " + str(xmin)), x=xmin-100, y=1)
    plt.plot(ys, color="y")
    pylab.ylim(-1.5, 1.5)
    plt.ylabel("Image Translated With Noise Added")
    plt.text(s=("Max: " + str(xmax)), x=xmax-100, y=1)

    plt.show()


def addNoise(xs):
    
    xs = list(map(lambda x: x + np.random.normal(0, 0.5), xs))
    return xs
    


def main():

    signal = gen_signal()
    
    frontzeros = random.randint(1000, 2000)
    backzeros = random.randint(1000, 2000)
    image = np.append(np.zeros(frontzeros), signal)
    image = np.append(image, np.zeros(backzeros))
    image = addNoise(image)


    # If you want to disable the display of minimum value, just change the below boolean to 'False'." 
    cross_correlate(signal, image, True)
    


main()





