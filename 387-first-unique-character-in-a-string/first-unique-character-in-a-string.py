from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)
        for index, val in enumerate(s):
            if d[val] ==1 :
                return index
        return -1


        