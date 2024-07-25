class Solution:
    def get_size(self, head):
        count = 1
        while head.next:
            count += 1
            head = head.next
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        size = self.get_size(head)
        take = k % size
        if take == 0:
            return head
        size = size - take
        temp = head
        while temp and size > 1:
            temp = temp.next
            size -= 1
        new_head = temp.next
        temp.next = None
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        return new_head
