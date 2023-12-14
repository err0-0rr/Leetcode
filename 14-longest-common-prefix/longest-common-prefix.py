class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num=0
        flag=0
        ls=list(map(len, strs))
        for i in range(len(strs[0])):
            alp=strs[0][i]
            for j in range(len(strs)):
                if ls[j]<=i or alp!=strs[j][i]:
                    flag=1
                    break
            if flag:
                break
            num+=1
        return strs[0][:num]