class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num={}
        ans={}
        for num in nums:
            count_num[num]=1+count_num.get(num,0)
        ans=sorted(count_num,key=lambda num:count_num[num],reverse=True)
        return ans[:k]
