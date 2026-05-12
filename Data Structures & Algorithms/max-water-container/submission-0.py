class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol_list=[]
        for i in range(len(heights)):
            temp=heights[i]
            for j in range(i+1,len(heights)):
                uchai=min(temp,heights[j])
                length=j-i
                vol=uchai*length
                vol_list.append(vol)
        return max(vol_list)
        