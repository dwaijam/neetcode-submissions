class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def checkpal(l, r)->int:
            count = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1

            return count
            
        count = 0
        for i in range(len(s)):
            count+=checkpal(i,i)
            if i<len(s)-1 and s[i]==s[i+1]:
                count+=checkpal(i,i+1)

        return count

        

        