class Solution:
    @staticmethod
    def get_size(head):
        count = 1
        while head.next:
            count += 1
            head = head.next
        return count

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = self.get_size(head)
        a = None
        b = None
        count = 1
        temp = head
        while temp:
            if count == k or count == size - k + 1:
                if a == None:
                    a = temp
                elif b == None:
                    b = temp
                else:
                    break
            temp = temp.next
            count += 1

        if a and b:
            a.val, b.val = b.val, a.val
        return head
