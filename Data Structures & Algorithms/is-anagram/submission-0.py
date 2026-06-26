class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for a in s:
            map[a] = map.get(a, 0) + 1
        
        for b in t:
            if b not in map:
                return False
            map[b]-=1
            if map[b] < 0:
                return False

        for v in map.values():
            if v > 0:
                return False
        return True