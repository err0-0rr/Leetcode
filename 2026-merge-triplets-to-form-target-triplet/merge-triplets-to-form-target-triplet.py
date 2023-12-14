class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # a=target.index(min(target))
        # if a==0:
        #     if target[1]<=target[2]:
        #         b,c=1,2
        #     else:
        #         b,c=2,1
        # if a==1:
        #     if target[0]<=target[2]:
        #         b,c=0,2
        #     else:
        #         b,c=2,0
        # if a==2:
        #     if target[0]<=target[1]:
        #         b,c=0,1
        #     else:
        #         b,c=1,0
        # #print(a,b,c)
        
        # triplets.sort(key = lambda x: (x[a], x[b], x[c]))
        #print(triplets)
        a=b=c=False
        for i,j,k in triplets:
            if i>target[0] or j>target[1] or k>target[2]:
                # if i>target[0] and j>target[1] and k>target[2]:
                #     break
                continue
            
            if i==target[0]:
                a=True
            if j==target[1]:
                b=True
            if k==target[2]:
                c=True
            
            if a and b and c:
                return True
            
        return False