class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in '+-*/' or len(token)>1:
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()
                if token=="+":
                    temp=a+b
                    stack.append(temp)
                elif token=='-':
                    temp=a-b
                    stack.append(temp)
                elif token=='*':
                    temp=a*b
                    stack.append(temp)
                elif token=='/':
                    temp=int(a/b)
                    stack.append(temp)
        return stack[-1]

        