class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        unique=set()
        max_length=0
        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length

            
        