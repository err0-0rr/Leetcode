class Solution:
    def knightDialer(self, n: int) -> int:
        mat=[[0 for i in range(n+1)] for j in range(10)]
        mod=(10**9)+7
        dic={
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
            
        }
        for i in range(10):
            mat[i][1]=1
            #mat[i][0]=0
        
        
        for i in range(2, n+1):
            for j in range(10):
                for k in dic[j]:
                    mat[j][i]+=mat[k][i-1]
                mat[j][i]=mat[j][i]%mod
                    
        ans=0
        for i in range(10):
            ans+=mat[i][n]
        return ans%mod