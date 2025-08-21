from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        longest = 0

        for num in s:  # iterate set directly (avoids duplicates)
            # only start counting if it's the beginning of a sequence
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                longest = max(longest, length)

        return longest
