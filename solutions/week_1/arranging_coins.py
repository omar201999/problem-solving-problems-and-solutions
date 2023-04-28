def arrangeCoins(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + n-(n-i)
        # print(f"sum in loop {sum}")
        if sum == n:
            print(i)
            break
        if sum > n:
            print(i-1)
            break


arrangeCoins(1303455736)
