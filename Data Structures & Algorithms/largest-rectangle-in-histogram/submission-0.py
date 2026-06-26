class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        mx = 0
        heights.append(0)
        for i in range(len(heights)):
            indextoins = i
            while st and heights[i] < st[-1][1]:
                last = st.pop()
                indextoins = last[0]
                mx = max(mx, (i - last[0]) * last[1])
            st.append([indextoins, heights[i]])

        return mx
            
            

