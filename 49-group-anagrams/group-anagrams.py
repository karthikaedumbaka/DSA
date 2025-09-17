class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d=dict()
        # if len(strs)==1:
        #     return [strs]
        # for s in strs:
        #     k="".join(sorted(s))
        #     if k in d:
        #         d[k].append(s)
        #     else:
        #         d[k]=[s]
        # return list(d.values())

        # # time O(n * k log k)
        # # space O(n *k)
        
        res = defaultdict(list)
        for s in strs:
            count =[0]*26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        return list(res.values())