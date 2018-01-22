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



def multimax_search(corrs):
    
    peaks = []
    argmax = np.argmax(corrs)
    single_max = corrs[argmax]
    threshold = .9*single_max
    peaks.append(argmax)

    for x in range(len(corrs)):
        if x == 0:
            if corrs[x] > corrs[x+1] and corrs[x] >= threshold:
                peaks.append(x)
                print(x)
        elif x == len(corrs)-1:
            if corrs[x] > corrs[x-1] and corrs[x] >= threshold:
                peaks.append(x)
                print(x)
        else:
            if (corrs[x] > corrs[x-1]) and (corrs[x] > corrs[x+1]) and corrs[x] >= threshold:
                peaks.append(x)
                print(x)
    return peaks





def cross_correlate(xs, ys, num_maxes=1, minval=False):
    """Takes two arrays and finds the x-value of the second at which both correlate highest.
        xs and ys are the first and second signals, respectively, with minval being a boolean
        declaring whether or not the x-value of minimum correlation should be found as well."""

    plt.subplot(211)
    plt.plot(xs, color="y")
    plt.ylabel("One-Dimensional Signal Pre-image")
    plt.subplot(212)



    corrs = []


    maxcorr = 0
    mincorr = 100
    for X in range(len(ys) - len(xs)):
        corr = 0
        for x in range(len(xs)):
            corr +=  (xs[x] * ys[x + X])
        corrs.append(corr)
   

    peaks = multimax_search(corrs)

    plt.plot(ys, color="y")
    pylab.ylim(-1.5, 1.5)
    plt.ylabel("Image Translated With Noise Added")
    
    for xmax in range(len(peaks)):
        plt.text(s=("Max: " + str(peaks[xmax])), x=peaks[xmax]-100, y=1)
        plt.axvline(x=peaks[xmax], linewidth=1, color='r')
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
    image = np.append(image, signal)
    image = np.append(image, np.zeros(backzeros))
    image = np.append(image, signal)
    image = addNoise(image)


    # If you want to disable the display of minimum value, just change the below boolean to 'False'." 
    cross_correlate(signal, image, 3)


main()





