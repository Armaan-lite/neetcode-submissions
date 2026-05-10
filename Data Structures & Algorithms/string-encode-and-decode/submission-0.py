class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_stuff=""
        for brush in strs:
            encoded_stuff+=str((len(brush)))+"#"+brush
        return encoded_stuff
        

    def decode(self, s: str) -> List[str]:
        decoded_stuff=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            decoded_stuff.append(word)
            i=j+1+length
        return decoded_stuff
