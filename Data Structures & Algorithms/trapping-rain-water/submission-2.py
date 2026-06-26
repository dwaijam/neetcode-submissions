class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        water = 0
        for i in range(len(height)): #3(3), 6(1),  - 6, 3
            if not st or height[i] < height[st[-1]]:
                st.append(i)
            else:
                temp = []
                while st and height[i] >= height[st[-1]]:
                    temp.append(st.pop())
                base = height[temp[0]]
                for c in temp[1:]:
                    water += (height[c]-base) * (i - c - 1)
                    base = height[c]
                if st:
                    water += (height[i]-base) * (i - st[-1] - 1)
                st.append(i)

        return water
