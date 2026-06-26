class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        min_int = -max_int - 1
        print(min_int)
        gen = False
        if x<0:
            neg = True
        ans = 0
        while x:
            dig = int(math.fmod(x, 10))
            x = int(x / 10)
            if ans > (max_int // 10) or (ans == (max_int // 10) and dig > (max_int %10)):
                return 0
            if ans < (min_int // 10) or ans == (min_int // 10) and dig < int(math.fmod(min_int, 10)):
                return 0
            ans = ans*10 + dig

        return ans
