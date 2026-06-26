class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        st = 0
        rep = 0
        ans = 0
        mx = 0
        # AAABBB
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            mx = max(mx, freq[s[i]])
            repl = i-st+1 - mx
            if i-st+1 - mx > k:
                freq[s[st]]-=1
                st+=1
            ans = max(ans, i-st+1)
        
        return ans

