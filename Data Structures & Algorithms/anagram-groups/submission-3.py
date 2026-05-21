class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupie=defaultdict(list)
        for s in strs:
            identity=''.join(sorted(s))
            groupie[identity].append(s)
        return list(groupie.values())
        