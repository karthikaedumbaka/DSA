class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        for i in range(min(len(word1),len(word2))):
            s.append(word1[i])
            s.append(word2[i])

        s="".join(s)
        if len(word1) < len(word2):
            s+=word2[len(word1):]
        else:
            s+=word1[len(word2):]
        return s
        