class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:
            if i=="C" :
                s.pop()
            elif i == "+":
                s.append(s[-1]+s[-2])
            elif i == "D":
                s.append(s[-1]*2)
            else:
                s.append(int(i))
                
        return sum(s)

# time O(n)
# space O(n)
        