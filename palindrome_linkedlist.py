class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse from middle
        p = None
        c = slow
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        #checking between front and middle
        while p and head:
            print(p.val, head.val)
            if p.val != head.val:
                return False
            p = p.next
            head = head.next
        return True
