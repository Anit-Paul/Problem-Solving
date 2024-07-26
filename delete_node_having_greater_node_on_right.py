# reverse the linked list
# then set the linked list in increasing order
# reverse the linked list to get the original order
# time O(n) space O(1)
class Solution:
    @staticmethod
    def __reverse(head):
        p=None
        c=head
        while c:
            temp=c.next
            c.next=p
            p=c
            c=temp
        return p
    def compute(self,head):
        #Your code here
        temp=self.__reverse(head)
        head=temp
        prev=temp
        temp=temp.next
        while temp:
            if(prev.data>temp.data):
                prev.next=temp.next
                temp=temp.next
            else:
                prev=prev.next
                temp=temp.next
        
        return self.__reverse(head)
