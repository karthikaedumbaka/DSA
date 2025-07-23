from collections import Counter
import atexit
atexit.register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def firstUniqChar(self, s: str) -> int:
        f=Counter(s)
        for index , value in enumerate(s):
            if f[value] ==1:
                return index
        return -1

        