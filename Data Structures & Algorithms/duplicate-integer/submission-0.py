class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for c in nums:
            if c in map:
                return True
            map[c] = True

        return False
         