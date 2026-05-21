class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+"#"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list=[]
        left=0
        right=len(s)-1
        while left<right:
            j=left
            while s[j]!= "#":
                j+=1
            length=int(s[left:j])
            word=s[j+1:j+1+length]
            decoded_list.append(word)
            left=j+length+1
        return decoded_list
