#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


class Solution:

    # @param A : integer
    # @return an integer

    def isPowerOfTwo(self, A):
        if A<0:
            return False
        A=bin(A)[2:]
        A=Counter([int(dig) for dig in A])
        return A.get(1,0) in [1]