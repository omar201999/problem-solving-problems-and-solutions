def sortedSquares(nums):
    sorted_list = []
    for i in nums:
        sorted_list.append(i ** 2)
    sorted_list = sorted(sorted_list)
    return sorted_list


print(sortedSquares([-7, -3, 2, 3, 11]))
