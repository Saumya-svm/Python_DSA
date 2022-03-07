def remove_zeroes(s):
    
    for i in range(len(s)):
        if s[i]!='0':
            return i


def convert_to_num(s,si,ss):
    if si>=len(s):
        return 0
    return convert_to_num(s,si+1,ss) + (10**((len(s)-si)))*(ord(s[si])-48)

s=input()
si=remove_zeroes(s)
if s=='0':
    print(convert_to_num(s,0,0)//10)
else:
    print(convert_to_num(s,si,0)//10)