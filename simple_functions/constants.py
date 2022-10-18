from numpy import sqrt
from simple_functions.functions1 import factorial
from functools import lru_cache

__all__ = ['pi']


def pi(terms=1):
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@cache
def rsum(n):
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
Then, lets add a new test file called test_constants.py. This should look something like the following:
import numpy as np

from simple_functions import pi


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = pi(2)
        assert np.isclose(my_pi, np.pi, atol=1e-12)