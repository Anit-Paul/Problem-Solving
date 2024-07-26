class Solution(object):
    def copyRandomList(self, head):
        map={}
        temp=head
        while temp:
            map[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            copy=map.get(temp)
            copy.next=map.get(temp.next)
            copy.random=map.get(temp.random)
            temp=temp.next
        return map.get(head)
