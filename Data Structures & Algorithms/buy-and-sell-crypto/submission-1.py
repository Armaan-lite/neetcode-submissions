class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen=[]
        profit=[]
        for i in range(len(prices)):
            if seen and prices[i]>min(seen):
                profit.append(prices[i]-min(seen))
            seen.append(prices[i])
        return max(profit) if profit else 0
        