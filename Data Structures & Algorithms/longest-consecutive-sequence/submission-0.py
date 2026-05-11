class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        work_set=nums
        counter=0
        longest=0
        for num in work_set:
            if num-1 not in work_set:
                counter=1
                while num+counter in work_set:
                    counter+=1
                longest=max(longest,counter)
        return longest