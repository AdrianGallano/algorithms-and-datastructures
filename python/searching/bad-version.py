# this implements binary search

def isBadVersion(n):
    # predefined list
    badVersions = [3,4,6,5]

    if n in badVersions:
        return True


def firstBadVersion(n: int) -> int:
    if isBadVersion(1):
        return n
    first = 1 
    last = n 
    while first+1 != last:
        mid = (first + last) // 2
        if isBadVersion(mid):
            last = mid
        else:
            first = mid
    return last