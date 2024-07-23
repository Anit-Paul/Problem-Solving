class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        count = count - n
        if count == 0:
            return head.next
        temp = head
        while count > 1:
            count -= 1
            temp = temp.next
        temp.next = temp.next.next
        return head
