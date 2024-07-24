class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 and l2:
            ans = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            temp.next = ListNode(ans)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            ans = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            temp.next = ListNode(ans)
            temp = temp.next
            l1 = l1.next
        while l2:
            ans = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            temp.next = ListNode(ans)
            temp = temp.next
            l2 = l2.next
        if carry != 0:
            temp.next = ListNode(carry)
        return dummy.next
