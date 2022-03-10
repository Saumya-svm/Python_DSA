
class PriorityQueueNode():

    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

class PriorityQueue():
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def __percolateUp(self):
        childIndex = self.getSize()

        while childIndex>0:
            parentIndex = (childIndex-1)//2
            if self.pq[parentIndex]>self.pq[childIndex]:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        index = 0
        l = len(self.pq)
        childIndex1 = 2*index + 1
        childIndex2 = 2*index + 2
        while True:
            minNodeIndex = index
            if self.pq[index].priority > self.pq[childIndex1].priority:
                minNodeIndex = childIndex1
            elif childIndex2<self.getSize() and self.pq[index].priority > self.pq[childIndex2].priority:
                minNodeIndex = childIndex2
            if minNodeIndex!=index: 
                self.pq[index],self.pq[minNodeIndex] = self.pq[minNodeIndex],self.pq[index] 
                index = minNodeIndex 
                leftIndex = 2*index + 1
                rightIndex = 2*index + 2
            else: 
                break
            



    def removeMin(self):
        if self.isEmpty():
            return None
        self.pq[0] = self.pop()
        self.__percolateDown(self)
        return minimum

while True:
    print('hwllo')
    break
        

