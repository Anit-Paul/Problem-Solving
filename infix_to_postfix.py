from collections import defaultdict
class Solution:
    def set_priority(self,map):
        map['^']=3
        map['*']=2
        map['/']=2
        map['+']=1
        map['-']=1
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        priority=defaultdict(int)
        self.set_priority(priority)
        ans=''
        n=len(exp)
        i=0
        stack=[]
        while i<n:
            if exp[i].isalpha() or exp[i].isdigit():
                ans+=exp[i]
                
            elif exp[i]=='(':
                stack.append(exp[i])
            elif exp[i]==')' :
                while stack and stack[-1]!='(':
                    ans+=stack.pop()
                stack.pop()
            else:
                while stack and priority[exp[i]]<=priority[stack[-1]] :
                    ans+=stack.pop()
                stack.append(exp[i])
            i+=1
        while stack:
            ans+=stack.pop()
        return ans
