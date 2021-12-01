# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:26:28 2021

@author: backm
"""

import numpy as np

def check_increasing(depths, window=1):
    """
    Parameters
    ----------
    depths : numpy.ndarray
        List of measured depths.
    window : int, optional
        Lenght of the window. The default is 1.

    Returns
    -------
    count : int
        Number of thimes the windowed-step depth is increased.

    """
    count = 0
    for i in range(len(depths)-window):
        prev = sum(depths[i:i+window])
        actual = sum(depths[i+1:i+1+window])
        if actual > prev:
            count += 1
    return count


if __name__ == '__main__':
    dd = np.loadtxt("input.txt")
    inc_window1 = check_increasing(dd)
    inc_window3 = check_increasing(dd, 3)
