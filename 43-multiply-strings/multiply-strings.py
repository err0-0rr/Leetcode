class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2=='0' or num1=='0':
            return "0"
        a,b=0,0
        val=ord('0')
        for i in num1:
            a=(a*10)+(ord(i)-val)
        for i in num2:
            b=(b*10)+(ord(i)-val)
        temp=a*b
        ans=""
        while temp>0:
            ans=chr((temp%10)+val)+ans
            temp=temp//10
        return ans