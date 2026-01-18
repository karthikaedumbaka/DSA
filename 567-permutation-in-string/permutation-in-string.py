from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # chcek the s1 is bigger that s2 the make it false
        if len(s1) > len(s2) :
            return False
        # make the counter to for s1 string and s2[:len(s1)]  and check whether bot counter are same 
        # if Yes make it true 
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:len(s1)])
        if s1_dict == s2_dict:
            return True    
        left = 0
        # make a left pointer at start of s2 string and right pointer at len(s1)
        # noe make a window for every loop increment the right pointer and decrement the left pointer value,
        # check if the left pointer value is equal to 0 , just pop() the value of left pointer
        # check or compare the counter if it is equal make it True or make it False
        for right in range(len(s1),len(s2)):
            s2_dict[s2[right]] += 1
            s2_dict[s2[left]] -=1
            if s2_dict[s2[left]] ==0:
                s2_dict.pop(s2[left])
            left+=1
            if s1_dict ==s2_dict:
                return True
        return False
        # time O(n)
        # space O(1)

# c = Solution()
# c.checkInclusion(s1 = "ab", s2 = "eidbaooo")







        