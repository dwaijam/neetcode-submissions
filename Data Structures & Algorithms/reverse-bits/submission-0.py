class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n, 'b')
        num = s.zfill(32)
        
        return int(num[::-1], 2)