def getParent(v,parent):
    if (v==parent[v]):
        return v
    return getParent(parent[v],parent)

def kruskal(edges,nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges,key = lambda edge:edge.wt)
    count = 0
    output= []
    i = 0
    while count<(nVertices-1):
        currentEdge = edges[i]
        sp = getParent(currentEdge.src,parent)
        dp = getParent(currentEdge.dest,parent)
        
        if sp!=dp:
            output.append(currentEdge)
            count +=1
            parent[sp]=dp
        i+=1
    return output

class Edge():
    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt

li = [int(i) for i in input().split()]
n = li[0]
e = li[1]
edges = []

for i in range(e):
    curr_input = [int(i) for i in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src,dest,wt)
    edges.append(edge)
output = kruskal(edges,n)
for edge in output:
    if edge.src<edge.dest:
        print(str(edge.src)+' '+ str(edge.dest)+' ' +str(edge.wt))
    else:
        print(str(edge.dest)+' '+ str(edge.src)+' '+ str(edge.wt))