from asyncio import constants
import random
from math import floor

randomNumber = random.SystemRandom()

def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x,floor(y/2),N)
    
    if y%2==0:
        return (z**2)%N
    else:
        return (x*(z**2))%N
	

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 1 - (1/(2**k))


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 1 -(1/(4**k))


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    
    for i in range(1, k+1):
        # get random int from 2 to n-1
        x = randomNumber.randint(2, N-1)
        mod = mod_exp(x, N-1, N)
        if mod == 1:
            if i == k:
                return 'prime'
        else:
            return 'composite'
    


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    for i in range(k):
        # get random int from 2 to n-1, not inclusive
        x = randomNumber.randint(2, N-1)
        # while N is even
        newN = N
        if(N%2 != 0):
            newN = N-1
        negativeSquare=1
        while newN % 2 == 0:
            result = mod_exp(x, newN, N)* negativeSquare
            if result-N == -1:
                negativeSquare = -1
                result = result*negativeSquare
            if (result == 1) | (result<0):
                newN /= 2
            else:
                return 'composite'
            
    return 'prime'

