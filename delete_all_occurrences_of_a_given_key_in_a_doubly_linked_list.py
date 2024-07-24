class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        while head and head.data==x:
            head=head.next
        head.prev=None
        dummy=head
        while head:
            if(head.data==x):
                temp=head.prev
                temp.next=head.next
                if(head.next):
                    head.next.prev=temp
            head=head.next
        return dummy
