class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        result = ""
        base_word = strs[0]
        for i in range(0,len(base_word)):
            for word in strs[1:]:
                if  i == len(word) or word[i] != base_word[i]:
                    return result
            result += base_word[i]
        return result
            
            
        