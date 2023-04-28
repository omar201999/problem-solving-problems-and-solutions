def BracketMatcher(str):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    if not str or str == " ":
        return False
    else:
        for i in str:
            if i == "(":
                counter1 += 1
            elif i == ")":
                counter1 -= 1
            elif i == "{":
                counter2 += 1
            elif i == "}":
                counter2 -= 1
            elif i == "[":
                counter3 += 1
            elif i == "]":
                counter3 -= 1
    if counter1 == 0 and counter2 == 0 and counter3 == 0:
        return True
    else:
        return False


print(BracketMatcher("([)]"))
