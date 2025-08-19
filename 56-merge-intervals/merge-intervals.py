class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # to sort the intervals 
        ans=[]
        i=0
        while i < len(intervals):
            s=intervals[i][0]  
            e=intervals[i][0]
            while  i < len(intervals) and intervals[i][0]<=e:
                # Dry run
                '''
                i=0 -> s=1,e=3 -> max: 3 == e;
                i=1 -> intervals[1][0]=2 ,e=3 -> max=6;
                i=2 ->  intervals[2][0]=8 , e=6 -> not overlap -> so append
                i=3 ->  intervals[3][0]=15 , e=6 -> not overlap -> so append

                '''
                e=max(e,intervals[i][1])
                i+=1
            ans.append([s,e])
        return ans
# TC : O(NlogN)
#space O(N)
        