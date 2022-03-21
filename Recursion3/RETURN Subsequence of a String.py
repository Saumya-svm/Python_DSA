def subsequences(string):
    if len(string) == 0:
        return ['']
    
    small = string[1:]
    ele = string[0]
    ss = subsequences(small)
    output=[]
    for i in ss:
        output.append(i)
    for i in ss:
        new = ele+i
        output.append(new)
        
    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)