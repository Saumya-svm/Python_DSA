def pairStar(s):
    if len(s) == (1 or 0):
        return s
    
    ns = pairStar(s[1:])
    if ns[0] == s[0]:
        return s[0]+'*'+ns
    else:
        return s[0]+ns

str = input()
print(pairStar(str))