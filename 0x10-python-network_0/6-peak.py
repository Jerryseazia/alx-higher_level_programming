#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    k = list_of_integers
    beg = 0
    end = len(k)-1

    if k[beg] > k[beg+1]:
        return k[beg]
    if k[end] > k[end-1]:
        return k[end]

    mid = (beg+end)//2
    if k[mid-1] < k[mid] and k[mid+1] < k[mid]:
        return k[mid]
    if k[mid] < k[mid-1]:
        return find_peak(k[beg:mid+1])
    elif k[mid] < k[mid+1]:
        return find_peak(k[mid:end+1])
    else:
        return k[beg]
