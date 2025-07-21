from math import ceil,floor
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=deque()
        for i in tokens:
            if i in '+-*/':
                b,a = stk.pop(),stk.pop()
                if i =="+":
                    stk.append(a+b)
                elif i=="-":
                    stk.append(a-b)
                elif i=='*':
                    stk.append(a*b)
                elif i=='/':
                    division = a/b
                    if division < 0 :
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(i))
        return stk[0]
        #time O(n)
        # space 0(n)

        