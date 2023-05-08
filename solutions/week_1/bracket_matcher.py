def BracketMatcher(str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in str:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return "NO"
        stack.pop()

    return "YES"


print(BracketMatcher("[([)]"))

# def BracketMatcher(str):
#    counter1 = 0
#    counter2 = 0
#    counter3 = 0
#    if not str or str == " ":
#        return False
#    else:
#        for i in str:
#            if i == "(":
#                counter1 += 1
#            elif i == ")":
#                counter1 -= 1
#            elif i == "{":
#                counter2 += 1
#            elif i == "}":
#                counter2 -= 1
#            elif i == "[":
#                counter3 += 1
#            elif i == "]":
#                counter3 -= 1
#    if counter1 == 0 and counter2 == 0 and counter3 == 0:
#        return True
#    else:
#        return False


# print(BracketMatcher("([)]"))
