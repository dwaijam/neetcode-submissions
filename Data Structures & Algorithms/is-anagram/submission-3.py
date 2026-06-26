class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)
        if len(s) != len(t):
            return False
        for ch in s:
            dic_s[ch]+=1
        for ch in t:
            dic_t[ch]+=1
        for k,v in dic_s.items():
            if dic_t[k]!=v:
                return False

        return True

