from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_Collection ={}
        magazineNote_Collection ={}
        ransomNote_Collection=Counter(ransomNote)
        magazineNote_Collection = Counter(magazine)
        for ransom in ransomNote:
            if ransom not in magazineNote_Collection:
                return False
            else:
                if (ransomNote_Collection[ransom] > magazineNote_Collection[ransom]):
                    return False
        return True 


# time O(n+m)
#space O(U+V)
        