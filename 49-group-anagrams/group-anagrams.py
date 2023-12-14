class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dic={}
        for i in strs:
            x=i
            temp=''.join(sorted(x))
            if temp not in dic:
                dic[temp]=[i]
            else:
                dic[temp]+=[i]
        
        for val in dic.values():
            ans.append(val)
        return ans