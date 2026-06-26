class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=''
        s = s.lower()
        for c in s:
            if c.isalnum():
                cleaned+=c

        return cleaned == cleaned[::-1]