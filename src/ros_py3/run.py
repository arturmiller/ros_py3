#!/usr/bin/env python

import numpy as np

def np_max(data):
    print 'func: np_max'
    return np.max(data)

if __name__ == '__main__':
    print('Hello World')
    print(np_max([1, 5, 4]))
