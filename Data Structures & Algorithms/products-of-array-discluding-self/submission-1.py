class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i in range(len(nums)):
            left=0
            right=len(nums)-1
            left_prod=1
            right_prod=1
            while left<i:
                left_prod=left_prod*nums[left]
                left+=1
            while i<right:
                right_prod=right_prod*nums[right]
                right-=1
            prod=left_prod*right_prod
            ans[i]=prod
        return ans

