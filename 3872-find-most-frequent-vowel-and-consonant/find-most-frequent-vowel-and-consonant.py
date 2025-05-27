
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vol="aeiou"
        u={}
        c={}
        for i in s: 
            if i in vol:
                u[i]=+u.get(i,0)+1
            else:
                c[i]=+c.get(i,0)+1
        max_vowel = max(u.values()) if u else 0
        max_consonant = max(c.values()) if c else 0

        return max_vowel+max_consonant