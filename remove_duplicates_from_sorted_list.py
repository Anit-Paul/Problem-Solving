class Solution(object):
    def deleteDuplicates(self, head):
        slow=head
        fast=head
        head=ListNode(0)
        dummy=head
        while fast:
            while fast and slow.val==fast.val :
                fast=fast.next
            if(slow.next==fast):
                dummy.next=slow
                dummy=dummy.next
                dummy.next=None
            slow=fast
        
        return head.next
