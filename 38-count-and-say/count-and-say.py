class Solution:
    def countAndSay(self, n: int) -> str:
        def util(s):
            ans=""
            n=len(s)
            i=0
            while i<n:
                num=s[i]
                count=1
                while i<n-1 and s[i+1]==num:
                    count+=1
                    i+=1
                ans+=str(count)+num
                i+=1
                #print(i)
            return ans
        if n==1:
            return "1"
        temp=n
        pre="1"
        while temp>1:
            pre=util(pre)
            temp-=1
        return pre



        
            