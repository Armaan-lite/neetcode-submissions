class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                last_temp,last_index=stack.pop()
                result[last_index]=i-last_index
            stack.append([t,i])
        return result


        