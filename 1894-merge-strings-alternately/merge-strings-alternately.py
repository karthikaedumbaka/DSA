class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        i,j,l,r=0,0,len(word1),len(word2)
        while i<l and j<r:
            result=result+word1[i]+word2[j]
            i+=1
            j+=1
        if i<l:
            while i<l:
                result=result+word1[i]
                i+=1
        if j<r:
            while j<r:
                result=result+word2[j]
                j+=1
        return result
            
# Time Complexity	O(m + n)
# Space Complexity	O(m + n)