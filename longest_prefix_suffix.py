class Solution:
	def lps(self, s):
	    arr=[0]*len(s)
		suf=1
		pre=0
		while suf<len(s):
		    if s[pre]==s[suf]:
		        arr[suf]=pre+1
		        suf+=1
		        pre+=1
		    else:
		        if pre==0:
		            arr[suf]=0
		            suf+=1
		        else:
		            pre=arr[pre-1]
		return arr[-1]
