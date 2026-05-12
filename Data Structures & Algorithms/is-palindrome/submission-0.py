class Solution:
    def isPalindrome(self, s: str) -> bool:
        work_s=""
        z=0
        while z<len(s):
            if not s[z].isalnum():
                z+=1
                continue
            work_s=work_s+s[z].lower()
            z+=1
        left=0
        right=len(work_s)-1
        while left<right:
            if work_s[left]!=work_s[right]:
                return False
            left+=1
            right-=1
        return True