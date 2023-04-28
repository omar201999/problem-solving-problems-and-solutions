def isPerfectSquare(num):
    num = num**0.5
    if num >= 1:
        if num % 1 == 0:
            return True
        else:
            return False
