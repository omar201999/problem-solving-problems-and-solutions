def search_insert_position(array, item):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if item == nums[mid]:
            return mid
        if item > nums[mid]:
            left = mid + 1
        else:
            right = mid-1
    return left


nums = [1, 3, 5, 6]
target = 8
print(search_insert_position(nums, target))
