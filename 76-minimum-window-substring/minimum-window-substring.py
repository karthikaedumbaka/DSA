from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case check if the t srting is null if it is null   or if the lenght of t is greater then length of s the return the output as ""
        if t=="" or len(t) > len(s):
            return ""
        # make the 2 dictionaries one the t count and make the dict for window
        t_count , window = Counter(t),defaultdict(int)
        have , need = 0,len(t_count)
        # the logic is sample check the key which are in t string and it is equal are not , if it is equal incerment the have to +1
        res,resLen = [-1,-1] , float("inf")
        l =0
        for r in range(len(s)):
            # take a c variable eo check currect char of s string
            c = s[r]
            # update to window dict with +=1
            window[c] +=1
            # now check the current char was present in t_count if yes check the value of current string  with our window dict and t_count dict
            # if the condition was correct increment  have variable to + 1
            if c in t_count and window[c] == t_count[c]:
                have += 1
            # now check have ==need it tell us all the char and leng for the t str are present in window dict 
            while have == need:
                # now slinky the window is the length of r and l is lessthan reslen if yes update it 
                if (r - l + 1 ) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1 )
                window[s[l]] -=1
                # important to check 
                # if any char was decrementing it make effeect the our problem condition 
                # so check the char of left pointer if the have of left pointer is less than to the t_dict the we need to decrment the have condition
                if s[l] in t_count and window[s[l]] < t_count[s[l]] :
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen !=float("inf") else ""
 

        