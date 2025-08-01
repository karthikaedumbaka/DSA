from collections import deque

class MinStack:

    def __init__(self):
        self.stk = deque()
        self.min_stk = deque()

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk :
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
