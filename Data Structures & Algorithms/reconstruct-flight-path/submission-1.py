class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        freq = defaultdict(int)
        for ticket in sorted(tickets)[::-1]:
            dic[ticket[0]].append(ticket[1])
            freq[ticket[0]]+=1

        ans = []
        st = []
        st.append("JFK")
        while st:
            cur = st[-1]
            if not dic[cur]:
                ans.append(st.pop())
            else:
                st.append(dic[cur].pop())

        return ans[::-1]
            