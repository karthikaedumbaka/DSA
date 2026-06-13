class Solution(object):
    def isPalindrome(self, s):
        l = 0 
        r = len(s)-1
        s = s.lower()
        

        def check(s,l,r):
            if l >= r:
                return True
            if not s[l].isalnum():
                return check(s,l+1,r)
            if not s[r].isalnum():
                return check(s,l,r-1)
            if not s[l] == s[r]:
                return False
            else:
                return check(s,l+1,r-1)
        return check(s,l,r)