class Solution:
    def trap(self, height: List[int]) -> int:
        max_water=0
        for i in range(len(height)):
            left=0
            right=len(height)-1
            max_height_left=0
            max_height_right=0
            while left<i:
                temp=height[left]
                max_height_left=max(temp,max_height_left)
                left+=1
            while i<right:
                temp=height[right]
                max_height_right=max(temp,max_height_right)
                right-=1
            cur_water=min(max_height_left,max_height_right)-height[i]
            if cur_water>=0:
                max_water+=cur_water
        return max_water

                
            
