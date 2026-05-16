class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1  #min rate
        right=max(piles)  #max rate
        result=right
        while left<=right:
            mid=(left+right)//2
            total_time=0
            for i in range(len(piles)):
                time=math.ceil(piles[i]/mid)
                total_time=total_time+time
            if total_time<=h:
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result




        