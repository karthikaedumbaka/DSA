
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_iter = iter(t)
        return all(char in t_iter for char in s)

        