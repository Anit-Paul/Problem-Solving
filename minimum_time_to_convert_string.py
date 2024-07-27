class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        inf = float('inf')
        dst=[[inf for _ in range(26)] for _ in range (26)]
        for i in range (len(original)):
            idx1=ord(original[i])-ord('a')
            idx2=ord(changed[i])-ord('a')
            dst[idx1][idx2]=min(dst[idx1][idx2],cost[i])
        for i in range(26):
            dst[i][i]=0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dst[i][j]=min(dst[i][j],dst[i][k]+dst[k][j])
        count=0
        for i in range(len(source)):
            idx1=ord(source[i])-ord('a')
            idx2=ord(target[i])-ord('a')
            if(dst[idx1][idx2]>=inf):
                return -1
            count+=dst[idx1][idx2]
        return count
