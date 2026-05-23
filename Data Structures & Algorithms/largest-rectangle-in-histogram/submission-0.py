class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and h<stack[-1][1]:
                index,height=stack.pop()
                length=i-index
                area=length*height
                max_area=max(max_area,area)
                start=index
            stack.append((start,h))
        for i,h in stack:
            length=len(heights)-i
            area=h*length
            max_area=max(max_area,area)
        return max_area
        