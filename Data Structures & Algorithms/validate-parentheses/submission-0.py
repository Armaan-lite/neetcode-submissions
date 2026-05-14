class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_To_open={')':'(','}':'{',']':'['}
        for c in s:
            if c in close_To_open:
                if stack and stack[-1]==close_To_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                
            

            
        