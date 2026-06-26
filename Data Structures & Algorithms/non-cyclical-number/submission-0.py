class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        while n!=1:
            res = 0
            while n>0:
                res+=(n%10)*(n%10)
                n = n //10
            if res in dic:
                return False
            dic.add(res)
            n = res

        return True
            