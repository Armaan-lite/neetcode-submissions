class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums=defaultdict(int)
        for num in nums:
            count_nums[num]=1+count_nums[num]
        ans=sorted(count_nums,key=lambda num:count_nums[num], reverse=True)
        return ans[:k]

        