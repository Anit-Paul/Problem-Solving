class Solution:
    #Function to merge K sorted linked list.
    def __merge(self,list1,list2):
        head=Node(0)
        dummy=head
        while list1!=None and list2!=None:
            if(list1.data<list2.data):
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        if(list1):
            dummy.next=list1
        if(list2):
            dummy.next=list2
        return head.next
    def mergeKLists(self,arr,K):
        if(len(arr)==0):
            return None
        while(len(arr)>1):
            list1=arr.pop(0)
            list2=arr.pop(0)
            arr.append(self.__merge(list1,list2))
        return arr[0]
