def removeX(string):
    if len(string)==0:
        return string
    s=removeX(string[1:])
    if string[0]=='x':
        return ''+s
    else:
        return string[0]+s

# Main
string = input()
print(removeX(string))