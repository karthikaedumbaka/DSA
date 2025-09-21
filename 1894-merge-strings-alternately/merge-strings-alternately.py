class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        result=''
        if len(word1)==0:
            return word2
        elif len(word2) == 0:
            return word1
        
        while i < len(word1) and i<len(word2):
            result+=word1[i]+word2[i]
            i+=1

        if i < len(word1):
            result+=word1[i:]
        else:
            result+=word2[i:]
        return result




        