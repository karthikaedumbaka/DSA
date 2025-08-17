class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            # if duplicate found, shrink window from left
            while s[r] in track:
                track.remove(s[l])
                l += 1
            # add current char to window
            track.add(s[r])
            # update answer
            ans = max(ans, r - l + 1)

        return ans
