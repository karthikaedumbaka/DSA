class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_num = []
        neg_num = []
        result=[]
        for n in nums:
            if n > 0:
                pos_num.append(n)
            else:
                neg_num.append(n)
        i=0
        while i < len(pos_num):
            result.append(pos_num[i])
            result.append(neg_num[i])
            i=i+1
        return result

        