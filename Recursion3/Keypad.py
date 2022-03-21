def getString(n):
    if n == 2:
        return 'abc'
    if n == 3:
        return 'def'
    if n == 4:
        return 'ghi'
    if n == 5:
        return 'jkl'
    if n == 6:
        return 'mno'
    if n == 7:
        return 'pqrs'
    if n == 8:
        return 'tuv'
    if n == 9:
        return 'wxyz'

def keypad(n):
    if n == 0:
        return ['']
    
    smallerNumber = n//10
    lastDigit = n%10
    
    s = keypad(smallerNumber)
    t = getString(lastDigit)
    output = []
    for i in s:
        for j in t:
            new = i+j
            output.append(new)
            
    return output
    

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)