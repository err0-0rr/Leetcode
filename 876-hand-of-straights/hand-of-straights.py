class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic={}
        for i in hand:
            try:
                dic[i]+=1
            except:
                dic[i]=1
        h=[]
        for i in dic.keys():
            heapq.heappush(h,i)
        
        count=len(h)
        
        while count:
            s=h[0]
            for i in range(s, s+groupSize):
                if i not in dic or dic[i]<=0:
                    return False
                else:
                    dic[i]-=1
                        
            while h and dic[h[0]]<=0:
                heapq.heappop(h)
                count-=1
                        
        return True