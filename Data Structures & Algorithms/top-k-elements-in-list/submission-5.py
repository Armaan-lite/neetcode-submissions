class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        sorted_counter={}
        for num in nums:
            counter[num]=1+counter.get(num,0)
        sorted_counter=sorted(counter,key=lambda num:counter[num],reverse=True)
        return sorted_counter[:k]