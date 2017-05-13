#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: recursion.py"""


def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if len(s1) == 1:
        if len(s2) == 1:
            if s1 == s2:
                return 0
            elif s1 > s2:
                return 1
            else:
                return -1
        else:
            return -1
    elif len(s2) == 1:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
