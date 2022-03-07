def removeConsecutiveDuplicates(s):
    if len(s) == 1:
        return s

    rcd = removeConsecutiveDuplicates(s[1:])
    if rcd[0] == s[0]:
        return s[0]+rcd[1:]
    else:
        return s[0]+rcd

str = input()
print(removeConsecutiveDuplicates(str))