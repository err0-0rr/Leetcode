class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(n):
            tot=0
            for i in piles:
                tot+=math.ceil(i/n)
                if tot>h:
                    return False
            return True
                 
        def bs(i, j):
            if i==j:
                return i
            mid=(i+j)//2
            #print(i, mid, j)
            if possible(mid):
                return bs(i, mid)
            return bs(mid+1, j)
            
        return bs(1, max(piles))