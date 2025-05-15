class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg=x<0
        x=abs(x)
        reversed_num=0
        while x>0:
            reversed_num = reversed_num * 10 + x%10
            x//=10
        if is_neg:
            reversed_num = -reversed_num
        if reversed_num < -2**31 or reversed_num>2**31-1:
            return 0
        return reversed_num

        


                
        