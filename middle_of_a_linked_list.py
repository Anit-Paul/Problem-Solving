class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        if head is None:
            return head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
