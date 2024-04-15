class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            try:
                dic[i]+=1
            except:
                dic[i]=1
        ls=[]
        for key, value in dic.items():
            ls.append([value, key])
        ls.sort(reverse=True)
        ans=""
        for a,b in ls:
            ans+=(b*a)
        return ans