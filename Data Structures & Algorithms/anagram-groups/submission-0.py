class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getMap(s: str) -> list:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')]+=1
            return arr

        dic = defaultdict(list)
        for s in strs:
            sig = getMap(s)
            print(sig)
            dic[tuple(sig)].append(s)

        return list(dic.values())

