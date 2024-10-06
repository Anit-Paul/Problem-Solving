class Solution:
    def is_prime(self,n):
        count=0
        i=1
        while i*i<=n:
            if n%i==0:
                count+=1
                if n/i!=i:
                    count+=1
            if count>2:
                return False
            i+=1
        return count==2
	def AllPrimeFactors(self, N):
		lst=[]
		i=1
        while i*i<=N:
		    if N%i==0:
		        if self.is_prime(i):
    		        lst.append(i)
    		    if (N//i)!=i and self.is_prime(N//i):
    		        lst.append(N//i)
		    i+=1
		return lst
