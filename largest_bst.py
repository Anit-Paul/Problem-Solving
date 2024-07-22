class Solution:
    def get_result(self,root):
        if root is None:
            return 0,float('inf'),float('-inf'),True
        lsize,lmin,lmax,lbst=self.get_result(root.left)
        rsize,rmin,rmax,rbst=self.get_result(root.right)
        if(lbst and rbst and lmax<root.data<rmin):
            return (lsize+rsize+1),min(lmin,root.data),max(rmax,root.data),True
        return max(lsize,rsize),float('-inf'),float('inf'),False
    def largestBst(self, root):
        size,min_val,max_val,is_bst=self.get_result(root)
        return size
