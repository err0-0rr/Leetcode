class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        ans=0
        for i in range(len(heights)-1):
            diff=heights[i]- heights[i+1]
            if diff>=0:
                ans+=1
            else:
                heapq.heappush(heap, diff)
                if abs(diff)<=bricks:
                    bricks-=abs(diff)
                    ans+=1
                elif ladders>0:
                    temp=-heapq.heappop(heap)
                    bricks+=(temp+diff)
                    ladders-=1
                    ans+=1
                else:
                    break
        #print(i, bricks, ladders)
        return ans