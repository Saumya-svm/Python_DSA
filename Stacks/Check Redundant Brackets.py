from sys import stdin

def checkRedundantBrackets(s) :
    c = 0
    
    
    for i in range(len(s)):
        print(s[i],c)
        if s[i] == '(':
            if s[i+1] == '(':
                c+=1
        if s[i] == ')':
            if s[i-1] not in '()':
                c-=1
        print(s[i],c)
    if c>0:
        return False
    elif c==0:
        return True

#main
expression = input()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")