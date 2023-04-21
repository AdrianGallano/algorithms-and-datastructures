def binary_search(l, target):
    top = 0
    bot = len(l) - 1

    while top <= bot:
        mid = (top + bot) // 2 

        if l[mid] > target: # 1 2 3 4 5 6 7
            bot = mid - 1
        elif l[mid] == target:
            return mid
        else:
            top = mid + 1
    return None

r = binary_search([1,2,3,4,5,6,7], 5)
print(r)