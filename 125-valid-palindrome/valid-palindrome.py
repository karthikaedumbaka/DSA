class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1
        return self.check(l,r,s)
    def check(self,l,r,s):
        if l >= r:
            return True
        if not s[l].isalnum():
            return self.check(l+1,r,s)
        if not s[r].isalnum():
            return self.check(l,r-1,s)
        if (s[l].lower()) != (s[r].lower()):
            return False
        return self.check(l+1,r-1,s)