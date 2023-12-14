class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        while num>0:
            if num>999:
                res+="M"
                num-=1000
            elif num>899:
                res+="CM"
                num-=900
            elif num>499:
                res+="D"
                num-=500
            elif num>399:
                res+="CD"
                num-=400
            elif num>99:
                res+="C"
                num-=100
            elif num>89:
                res+="XC"
                num-=90
            elif num>49:
                res+="L"
                num-=50
            elif num>39:
                res+="XL"
                num-=40
            elif num>9:
                res+="X"
                num-=10
            elif num==9:
                res+="IX"
                num-=9
            elif num>4:
                res+="V"
                num-=5
            elif num==4:
                res+="IV"
                num-=4
            else:
                res+="I"
                num-=1
                
        return res
            