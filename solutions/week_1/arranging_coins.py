def arrangeCoins(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + n-(n-i)
        print("$" * i, end="\n")
        # print(f"sum in loop {sum}")
        if sum == n:
            return i
        if sum > n:
            return i-1


print(arrangeCoins(5))
