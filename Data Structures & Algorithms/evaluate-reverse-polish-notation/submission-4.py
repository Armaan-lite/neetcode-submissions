class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper={"+","-","*","/"}
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in oper:
                stack.append(int(tokens[i]))
            else:
                a=stack[-2]
                b=stack[-1]
                if tokens[i]=="+":
                    ans=a+b
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if tokens[i]=="-":
                    ans=a-b
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if tokens[i]=="*":
                    ans=a*b
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
                if tokens[i]=="/":
                    ans=int(a/b)
                    stack.pop()
                    stack.pop()
                    stack.append(ans)
        ans=stack.pop()
        return ans



        