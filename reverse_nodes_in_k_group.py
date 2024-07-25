class Solution:
    def reverse(self, head):
        p = None
        c = head
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        return p

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        count = 1
        if head == None or head.next == None or k == 1:
            return head
        a = None
        b = None
        temp = head
        while temp:
            if count == k:
                x = temp.next
                temp.next = None
                if a == None:
                    a = self.reverse(start)
                    b = start

                else:
                    b.next = self.reverse(start)
                    b = start
                temp = x
                start = temp
                count = 0
            else:
                temp = temp.next
            count += 1
        if count != k or temp == None:
            b.next = start
        return a
