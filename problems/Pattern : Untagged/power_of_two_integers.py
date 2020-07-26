#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


class Solution:

    # @param A : integer
    # @return an integer

    def isPower(self, A):
        power_of_prime_factors = {}
        temp=A
        if A==1:
            return 1
        while temp % 2 == 0:
            if not power_of_prime_factors.has_key(2):
                power_of_prime_factors[2] = 0
            power_of_prime_factors[2] = power_of_prime_factors[2] + 1
            temp=temp//2
        for prime_no in range(3, int(math.sqrt(A))+1, 2):
            temp=A
            if not isPrime(prime_no):
                continue
            while temp % prime_no == 0:
                if not power_of_prime_factors.has_key(prime_no):
                    power_of_prime_factors[prime_no] = 0
                power_of_prime_factors[prime_no] += 1
                temp=temp//prime_no
        #print(power_of_prime_factors)
        #if len(set(power_of_prime_factors.values())) != 1:
        #    return 0
        if 1 in power_of_prime_factors.values():
            return 0
        return 1

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

