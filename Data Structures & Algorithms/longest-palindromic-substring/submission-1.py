class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = ""
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    break
                if r-l+1 > len(mx):
                    mx = s[l:r+1]
                l-=1
                r+=1
            
            if i<len(s)-1 and s[i] == s[i+1]:
                l=i
                r=i+1
                while l>=0 and r<len(s):
                    if s[l]!=s[r]:
                        break
                    if r-l+1 > len(mx):
                        mx = s[l:r+1]
                    l-=1
                    r+=1
        return mx


        