class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for str in strs:
            temp=''.join(sorted(str))
            if temp not in hashmap:
                hashmap[temp]=[]
            hashmap[temp].append(str)
        return list(hashmap.values())