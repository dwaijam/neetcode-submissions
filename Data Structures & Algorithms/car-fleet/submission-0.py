class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dp = list(map(lambda a, b: [a, b], position, speed))
        dp.sort(key=lambda x: x[0])
        st = []
        for j in range(len(dp)-1, -1, -1):
            car = dp[j]
            time = (target - car[0]) / car[1]
            if not st or time > st[-1]:
                st.append(time)

        return len(st)
