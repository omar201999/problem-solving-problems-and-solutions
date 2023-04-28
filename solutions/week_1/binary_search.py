def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low+high) // 2
        print(mid)
        print(high)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(binary_search(nums, target))
