class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        dic={'M':0,'P':0,'G':0}
        act=set()
        ans=0
        for i in range(len(garbage)-1, -1, -1):
            ans+=len(garbage[i])
            if len(act)!=3:
                s=set(garbage[i])
                for c in s:
                    if dic[c]==0:
                        dic[c]=i
                        act.add(c)
    
        travel.insert(0,0)
        for i in range(2, min(len(travel), max(dic.values())+1)):
            travel[i]+=travel[i-1]
        #print(ans, dic, travel)
        ans+=(travel[dic['M']]+travel[dic['P']]+travel[dic['G']])
        return ans