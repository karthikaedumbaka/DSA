# from collections in defaultdict
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        p_dict = Counter(p)
        s_dict = Counter(s[:len(p)])
        reslut = [0] if p_dict == s_dict else []

        for right in range(len(p),len(s)):
            s_dict[s[right]] +=1
            s_dict[s[left]] -=1

            if s_dict[s[left]] ==0:
                s_dict.pop(s[left])
            left +=1
            
            if p_dict == s_dict:
                reslut.append(left)
        
        return reslut
            

            
                
