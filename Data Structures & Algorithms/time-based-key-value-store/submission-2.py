class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lis = self.map[key]
        print(lis)
        if not lis:
            return ""
        l=0
        r=len(lis)
        while l<r:
            mid = (l+r)//2
            mid_num = lis[mid][0]
            if mid_num == timestamp:
                return lis[mid][1]
            elif timestamp > mid_num:
                l=mid+1
            else:
                r = mid
        mid = max(l-1, 0)
        if timestamp >= lis[mid][0]:
            return lis[mid][1]
        else:
            return ""
        

"""
1-a 2-b 4-c
"""