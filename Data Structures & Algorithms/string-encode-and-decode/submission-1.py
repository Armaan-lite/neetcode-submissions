class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string=""
        for risk in strs:
            encode_string+=str(len(risk))+"$"+risk
        return encode_string

    def decode(self, s: str) -> List[str]:
        decoded_strings=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="$":
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            decoded_strings.append(word)
            i=j+1+length
        return decoded_strings