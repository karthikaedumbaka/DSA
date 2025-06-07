class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m=len(needle)
        for i in range(0,n):
            j=0
            for k in range(i,n):
                if haystack[k] == needle[j]:
                    j+=1
                else :
                    break 
                if j==m:
                    return i
        return -1