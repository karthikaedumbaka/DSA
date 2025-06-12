class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        if len(strs)==1:
            return [strs]
        for s in strs:
            k="".join(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k]=[s]
        return list(d.values())

        # time O(n)
        # space O(n)
        