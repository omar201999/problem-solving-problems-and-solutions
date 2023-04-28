def guessNumber(n):
    low = 0
    high = n
    state = True

    while state:
        mid = (low+high)//2
        print(f"is this your guess num : {mid}")
        var = int(input())
        if var == 0:
            state = False
            return mid
        if var == -1:
            high = mid - 1
        if var == 1:
            low = mid + 1


print(guessNumber(10))
