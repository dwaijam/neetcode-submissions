class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        lis = [[] for _ in range(l)]
        map = {}
        for c in nums:
            map[c] = map.get(c,0)+1
        
        for key,val in map.items():
            lis[val-1].append(key)
        print(lis)
        
        i = l-1
        res = []
        while len(res) < k:
            if(lis[i]):
                res.extend(lis[i])
            i-=1

        return res