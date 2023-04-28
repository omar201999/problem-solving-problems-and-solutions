def isPalindrome(s):
    only_letters = ''.join(filter(str.isalpha, s)).lower()
    left = 0
    right = len(only_letters)-1
    if len(only_letters) == 1:
        return False
    while left < right:
        if only_letters[left] == only_letters[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome("a"))


def isPalindromeAnotherSolution(s):
    only_letters = ''.join(filter(str.isalpha, s)).lower()
    revers_letter = only_letters[::-1]
    if len(only_letters) == 1:
        return False
    if only_letters == revers_letter:
        return True
    else:
        return False


print(isPalindromeAnotherSolution("a"))


def isPalindromeAnotherSolutions(s):
    st = ''
    for i in s:
        if i.isalnum():
            st += i.lower()
    if st == st[::-1]:
        return True


print(isPalindromeAnotherSolutions(""))
