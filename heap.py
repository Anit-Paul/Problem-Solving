class heap:
    def __init__(self):
        self.arr=[None]*1000
        self.size=0
        
    def insert(self,data):
        self.arr[self.size]=data
        self.size+=1
        parent=(self.size-1)//2
        i=self.size-1
        while parent!=0 and self.arr[parent]<self.arr[i]:
            self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
            i=parent
            parent=(i-1)//2
        if parent==0 and self.arr[i]>self.arr[parent]:
            self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
            
    def display(self):
        print(self.arr[:self.size])
        
    def delete(self):
        self.arr[0]=self.arr[self.size-1]
        self.size-=1
        i=0
        while i<self.size:
            left=2*i+1
            right=2*i+2
            if left<self.size and self.arr[left]>self.arr[i]:
                self.arr[i],self.arr[left]=self.arr[left],self.arr[i]
                i=left
            elif right<self.size and self.arr[right]>self.arr[i]:
                self.arr[i],self.arr[right]=self.arr[right],self.arr[i]
                i=right
            else:
                break
        
    
def heapify(i,arr):
    left=2*i+1
    right=2*i+2
    largest=i
    size=len(arr)
    if left<size and arr[left]>arr[largest]:
        largest=left
    if right<size and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(largest,arr)


a=heap()
a.insert(4)
a.insert(8)
a.insert(7)
a.insert(2)
a.insert(9)
a.insert(400)
a.insert(70)
a.insert(20)
a.display()
a.delete()
for i in range(((a.size)//2),-1,-1):
    heapify(i,a.arr[:a.size])

a.display()
