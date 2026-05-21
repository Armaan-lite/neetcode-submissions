class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        cur_area=0
        max_area=0
        while left<right:
            h=min(heights[left],heights[right])
            l=right-left
            cur_area=h*l
            max_area=max(cur_area,max_area)
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
        return max_area

        