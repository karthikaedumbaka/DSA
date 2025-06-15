class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                ch = st.pop()
                if (i == '}' and ch != '{') or (i == ']' and ch != '[') or (i == ')' and ch != '('):
                    return False
        return len(st) == 0
