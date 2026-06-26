class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        maxi = 0
        st = 0
        for i in range(len(s)):
            if s[i] in freq:
                while st < i and s[st]!=s[i]:
                    del freq[s[st]]
                    st+=1
                st+=1
            else:
                freq[s[i]] = True
            maxi = max(maxi, i - st+1)

        return maxi
                

        