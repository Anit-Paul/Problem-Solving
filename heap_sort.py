def heap_sort(arr):
    n=len(arr)-1
    while n>0:
        heapify(arr,n)
        arr[0],arr[n]=arr[n],arr[0]
        n-=1
        
def heapify(arr,n):
    for i in range((n+1)//2,-1,-1):
        compute_heapify(i,arr,n)
    
def compute_heapify(i,arr,n):
    left=2*i+1
    right=2*i+2
    largest=i
    size=n+1
    if left<size and arr[left]>arr[largest]:
        largest=left
    if right<size and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        compute_heapify(largest,arr,n)

lst=[54,12,45,62,10,14,85,3,20,0,14]
heap_sort(lst)
print(lst)