class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        def fun(x):
            return x[1]
        ls=sorted(dic.items(), key=fun, reverse=True)
        ls=ls[:k]
        for i in range(k):
            ls[i]=ls[i][0]
        return ls
        