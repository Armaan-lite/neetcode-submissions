class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        chums=sorted(nums)
        ans=[]
        for i in range(0,len(chums)-2):
            if i>0 and chums[i]==chums[i-1]:
                continue
            left=i+1
            right=len(chums)-1
            while left<right:
                sum=chums[left]+chums[i]+chums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    sum==0
                    ans.append([chums[left],chums[i],chums[right]])
                    left+=1
                    while left<right and chums[left]==chums[left-1]:
                        left+=1
        return ans
            
        
        
        