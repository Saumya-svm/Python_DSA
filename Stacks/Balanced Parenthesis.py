def isBalanced(string):
    stack = []
    for char in string:
        if char in '({[':
            stack.append(char)
        elif char == ')':
            if (not stack or stack[-1]!='('):
                return False
            stack.pop()
        elif char == '}':
            if (not stack or stack[-1]!='{'):
                return False
            stack.pop()
        elif char == ']':
            if (not stack or stack[-1]!='['):
                return False
            stack.pop()
    if (not stack):
        return True
    else:
        return False
    
string = input()
ans = isBalanced(string)
if ans:
    print('true')
else:
    print('false')