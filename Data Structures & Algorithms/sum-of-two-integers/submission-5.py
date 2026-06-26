class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while a!=0:
            carry = (a & b ) << 1
            b = (a ^ b ) & mask
            a = carry & mask

        return b if b <= max_int else ~(b ^ mask)