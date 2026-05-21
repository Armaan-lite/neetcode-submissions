class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s=defaultdict(int)
        count_t=defaultdict(int)
        for c in s:
            count_s[c]=1+count_s[c]
        for c in t:
            count_t[c]=1+count_t[c]
        for n in count_s:
            if count_s[n]!=count_t[n]:
                return False
        return True
        