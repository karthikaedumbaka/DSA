class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # storing the values for the roman keys in dict
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        n=len(s)
        summ=0
        i=0
        while  i<n:
            # check the i is lessthan n-1 and also check the next roman ltters is lessthan it 
            if i<n-1 and d[s[i]]<d[s[i+1]]:
                
                summ+= d[s[i+1]] -d[s[i]]
                i+=2
            else:
                summ=summ + d[s[i]]
                i+=1
        return summ
