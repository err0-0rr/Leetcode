class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic={}
        for i in tasks:
            try:
                dic[i]-=1
            except:
                dic[i]=-1
        h=[]
        for i in dic.values():
            heapq.heappush(h, i)
        q=deque()
        ans=0
        while len(h)>0 or len(q)>0:
            ans+=1
            #print(h, q)
            if q and -q[0][1]<ans:
                x=q.popleft()
                heapq.heappush(h,x[0])
            if h:
                temp=(heapq.heappop(h)+1, -ans-n)
                if temp[0]!=0:
                    q.append(temp)
        return ans