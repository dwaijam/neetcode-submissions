class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = []
        c = Counter(nums)
        for n in nums:
            if n-1 not in c:
                st.append(n)
        
        ans = 0
        print(st)
        for s in st:
            if s not in c:
                continue
            count = 1
            next = s + 1
            while next in c:
                count+=1
                del c[next]
                next+=1
            ans = max(ans, count)
        
        return ans
            
