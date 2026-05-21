class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        cur_area=0
        for i in range(len(heights)):
            temp=heights[i]
            for j in range(i+1,len(heights)):
                uchai=min(temp,heights[j])
                length=j-i
                cur_area=uchai*(j-i)
                max_area=max(max_area,cur_area)
        return max_area

        