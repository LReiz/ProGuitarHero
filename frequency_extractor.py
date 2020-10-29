import numpy as np
from scipy.signal import butter, lfilter, fftconvolve

"""
	Module taken from the following project: https://github.com/codyd51/offkeyboard
"""

def find(condition):
    # https://stackoverflow.com/questions/57100894/matplotlib-versions-3-does-not-inlclude-a-find
    res, = np.nonzero(np.ravel(condition))
    return res

def parabolic(f, x):
    """Quadratic interpolation for estimating the true position of an
    inter-sample maximum when nearby samples are known.
    f is a vector and x is an index for that vector.
    Returns (vx, vy), the coordinates of the vertex of a parabola that goes
    through point x and its two neighbors.
    Example:
    Defining a vector f with a local maximum at index 3 (= 6), find local
    maximum if points 2, 3, and 4 actually defined a parabola.
    In [3]: f = [2, 3, 1, 6, 4, 2, 3, 1]
    In [4]: parabolic(f, argmax(f))
    Out[4]: (3.2142857142857144, 6.1607142857142856)
    """
    xv = 1 / 2. * (f[x - 1] - f[x + 1]) / (f[x - 1] - 2 * f[x] + f[x + 1]) + x
    yv = f[x] - 1 / 4. * (f[x - 1] - f[x + 1]) * (xv - x)
    return (xv, yv)

def freq_from_autocorr(sig, fs):
    """Estimate fundamental frequency using autocorrelation
    From: https://gist.github.com/endolith/255291
    """
    # Calculate autocorrelation (same thing as convolution, but with
    # one input reversed in time), and throw away the negative lags
    corr = fftconvolve(sig, sig[::-1], mode='full')
    corr = corr[len(corr)//2:]


    # Find the first low point
    d = np.diff(corr)
    if(not (max(d) < 0)):
        start = find(d > 0)[0]

        # Find the next peak after the low point (other than 0 lag).  This bit is
        # not reliable for long signals, due to the desired peak occurring between
        # samples, and other peaks appearing higher.
        # Should use a weighting function to de-emphasize the peaks at longer lags.
        peak = np.argmax(corr[start:]) + start
        px, py = parabolic(corr, peak)

        return fs / px
    return False