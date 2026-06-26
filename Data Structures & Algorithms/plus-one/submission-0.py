class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev = digits[::-1]
        carry = 1
        for i in range(len(rev)):
            sm = carry + rev[i]
            rev[i] = sm%10
            carry = sm//10
        if carry>0:
            rev.append(carry)
        
        return rev[::-1]
        