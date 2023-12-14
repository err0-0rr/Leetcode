class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def fun(x):
            return x[0]
        intervals.sort(key=fun)
        ans=[intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0]<=ans[-1][1]:
                mini=min(ans[-1][0], intervals[i][0])
                maxi=max(intervals[i][1], ans[-1][1])
                ans.pop()
                ans.append([mini, maxi])
                continue
            ans.append(intervals[i])
        return ans