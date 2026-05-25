class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate=max(piles)
        min_rate=1
        while min_rate<max_rate:
            time=0
            rate=(min_rate+max_rate)//2
            for pile in piles:
                time+=math.ceil(pile/rate)
            if time>h:
                min_rate=rate+1
            else:
                max_rate=rate
        return min_rate
        