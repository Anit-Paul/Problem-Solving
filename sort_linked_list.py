class Solution:
    def get_mid(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        head = ListNode(0)
        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                lst = ListNode(list1.val)
                temp.next = lst
                list1 = list1.next
            else:
                lst = ListNode(list2.val)
                temp.next = lst
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return head.next

    def compute_sort(self, head):
        if head == None or head.next == None:
            return head
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None
        lst1 = self.compute_sort(left)
        lst2 = self.compute_sort(right)
        return self.merge(lst1, lst2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.compute_sort(head)
