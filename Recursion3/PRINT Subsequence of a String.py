def subsequences(string,output=['']):
    if len(string) == 0:
        for i in output:
            if i!='':
                print(i)
        return
    
    l = output
    m = []
    for i in l:
        m.append(i)

    ele = string[0]
    for i in l:
        new = i+ele
        m.append(new)
    subsequences(string[1:],m)
    
string = input()
ans = subsequences(string)