class Solution:
    
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        prev=head
        pres=head.next
        while pres:
            if(pres.data==prev.data):
                prev.next=pres.next
                if(pres.next):
                    pres.next.prev=prev

            else:
                prev=prev.next
            pres=pres.next
        return head
