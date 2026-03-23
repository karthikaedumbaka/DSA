from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = defaultdict(int)
        result = ""
        for i in s:
            count_dict[i] +=1
        count_dict
        sort_dic = sorted(count_dict.items(),key=lambda x : x[1],reverse = True)
        for i,count in sort_dic:
            result += (i*count)
        return result
        