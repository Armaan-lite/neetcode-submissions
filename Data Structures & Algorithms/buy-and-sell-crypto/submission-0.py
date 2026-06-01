class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        for i in range(len(prices)):
            temp=prices[i]
            sell_list=[]
            for j in range(i+1,len(prices)):
                if prices[j]>temp:
                    sell_list.append(prices[j])
            if sell_list:
                max_return=max(sell_list)
                profits.append(max_return-temp)
        return max(profits) if profits else 0



