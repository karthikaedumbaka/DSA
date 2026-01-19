from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans =0 
        limit = defaultdict(int)

        left,right =0,0
        while right < len(fruits):
            limit[fruits[right]] +=1 
            if len(limit) <= 2:
                ans = max(ans, right - left +1)
            else:
                while left < right:
                    limit[fruits[left]] -=1
                    if limit[fruits[left]] == 0:
                        limit.pop(fruits[left])
                    left+=1
                    if  len(limit) <= 2:
                        break
            
            right +=1
        return ans

                

        