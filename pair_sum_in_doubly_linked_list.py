class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        if(head==None):
            return []
        low=head
        temp=head
        res=[]
        while(temp.next):
            temp=temp.next
        high=temp
        while(low!=high and low.prev!=high):
            sum=low.data+high.data
            if(sum>target):
                high=high.prev
            elif(sum<target):
                low=low.next
            else:
                res.append([low.data,high.data])
                low=low.next
                high=high.prev
        return res
