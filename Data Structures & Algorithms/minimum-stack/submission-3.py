class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.minval=0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minval=min(val,self.minstack[-1])
            self.minstack.append(self.minval)
        else:
            self.minstack.append(val)
        return self
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        return self
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minstack[-1]
        
