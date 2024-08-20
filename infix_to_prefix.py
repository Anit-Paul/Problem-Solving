class solution:
    
    @staticmethod
    def __reverse(s : str)->str:
        rs=''
        for char in s :
            if char=='(':
                rs=')'+rs
            elif char==')':
                rs='('+rs
            else:
                rs=char+rs
        return rs
    
    def priority(self,char)->int:
        if char=='^':
            return 3
        if char=='*' or char=='/':
            return 2
        if char=='+' or char=='-':
            return 1
        return -1
    
    def __infix_to_postfix(self,s:str)->str:
        res=''
        stack=[]
        for char in s:
            if char.isdigit() or char.isalpha():
                res+=char
            elif char=='(':
                stack.append(char)
            elif char==')':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.pop()
            else:
                while stack and self.priority(char)<self.priority(stack[-1]):
                    res+=stack.pop()
                stack.append(char)
        while stack:
            res+=stack.pop()
        return res
                
                
    def compute_prefix(self,s:str)->str:
        s=solution.__reverse(s)
        s=self.__infix_to_postfix(s)
        return solution.__reverse(s)
        



def main():
    s=input('enter the infix equation : ')
    a=solution()
    print(a.compute_prefix(s))
if __name__=='__main__':
    main()
