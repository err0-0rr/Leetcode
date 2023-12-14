class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mini=newInterval[0]
        maxi=newInterval[1]
        def checkfun(i):
            if i!=len(intervals)-1:
                if intervals[i+1][0]>=intervals[i][0] and intervals[i+1][0]<=intervals[i][1]:
                    intervals[i][0]=min(intervals[i][0], intervals[i+1][0])
                    intervals[i][1]=max(intervals[i][1], intervals[i+1][1])
                    intervals.pop(i+1)
                    checkfun(i)
            return 

        for i in range(len(intervals)):
            if mini>intervals[i][0] and mini>intervals[i][1]:
                continue
            if mini<intervals[i][0] and maxi<intervals[i][1]:
                intervals.insert(i, newInterval)
                checkfun(i)
                return intervals
            nmin=min(mini, intervals[i][0])
            nmax=max(maxi, intervals[i][1])
            intervals.pop(i)
            intervals.insert(i, [nmin, nmax])
            checkfun(i)
            return intervals
        intervals.append(newInterval)
        return intervals