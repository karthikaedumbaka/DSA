from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        # return list(res.values())

        # bf 
        # group_dict = {}
        # for word in strs :
        #     sorted_str = "".join(sorted(word))
        #     if sorted_str  not in group_dict:
        #         group_dict[sorted_str]  = []
        #     group_dict[sorted_str].append(word)
        # return list(group_dict.values())
        # but take O(m.nlogn)
        '''
        why ? , because we are using sorting , it take N(logN) for each word in a strs
        and m for no.of word in a strs )
        '''
        output = defaultdict(list)
        for word in strs:
            res = [0]*26 # why 26 because we have only 26 letter in english alphabets
            for i in word :
                res[ord(i) - ord('a')] +=1
            output[tuple(res)].append(word)
        return list(output.values())
