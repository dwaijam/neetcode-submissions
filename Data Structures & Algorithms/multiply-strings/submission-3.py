class Solution:
    def multiply(self, num1: str, num2: chr) -> str:
        if num1 == "0" or num2 =="0":
            return "0"
       


        def mul(num1: str, num2: str) -> str:
            r1 = num1[::-1]
            i = 0
            carry = 0
            res = []
            multiplier = int(num2)
            while i < len(r1):
                sum=multiplier * int(r1[i]) + carry
                res.append(str(sum%10))
                carry = sum//10
                i+=1
            if carry>0:
                res.append(str(carry))
            
            return ''.join(res[::-1])

        def add(num1: str, num2: str) -> str:
            if len(num1) < len(num2):
                return add(num2, num1)
            r1 = num1[::-1]
            r2 = num2[::-1]
            i = 0
            carry = 0
            res = []
            sum = 0
            while i < len(r1):
                sum=int(r1[i]) + carry
                if i < len(r2):
                    sum+=int(r2[i])
                res.append(str(sum%10))
                carry = sum//10
                i+=1
            if carry>0:
                res.append(str(carry))
            
            return ''.join(res[::-1])

        res = ""
        ten = ""
        for c in num1[::-1]:
            inter = mul(num2,c) + ten
            ten = ten+"0"
            res = add(res, inter)

        return res
                
