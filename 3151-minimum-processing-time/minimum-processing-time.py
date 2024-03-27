class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans=0
        temp=0
        for i in processorTime:
            for j in range(4):
                ans=max(ans, i+tasks[temp+j])
            temp+=4
        return ans