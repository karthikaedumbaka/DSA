class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s=float("inf") # to get the highest possible +ve integer 
        for i in strs:# checking every value in a string
        # check every element string in strs if the lenght is lessthan then it will sort 
            if len(i) < s:  
                s=len(i)
        for i in range(0,s):
            for strings in strs:
                if strings[i]!=strs[0][i]:
                    return strings[:i]
                
        return strs[0][:s]