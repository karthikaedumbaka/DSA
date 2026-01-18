from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:len(s1)])
        if s1_dict == s2_dict:
            return True

        left = 0
        
        

        for right in range(len(s1),len(s2)):
            s2_dict[s2[right]] += 1
            s2_dict[s2[left]] -=1

            if s2_dict[s2[left]] ==0:
                s2_dict.pop(s2[left])
            left+=1
            if s1_dict ==s2_dict:
                return True
        return False

c = Solution()
c.checkInclusion(s1 = "ab", s2 = "eidbaooo")




        