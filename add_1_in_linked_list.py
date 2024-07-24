class Solution:
    def reverse_list(self,head):
        p=None
        c=head
        while c:
            temp=c.next
            c.next=p
            p=c
            c=temp
        return p
    def addOne(self,head):
        #Returns new head of linked List.
        head=self.reverse_list(head)
        temp=head
        prev=head
        while(temp and temp.data==9):
            temp.data=0
            prev=temp
            temp=temp.next
        if(temp==None):
            prev.next=Node(1)
        else:
            temp.data+=1
        return self.reverse_list(head)
