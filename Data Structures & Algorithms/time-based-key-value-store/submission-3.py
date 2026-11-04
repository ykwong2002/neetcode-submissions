class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.d.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if self.d[key][m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1
        
        return res

"""
Goal: define functions to return the value at key AND timestamp. if not present, return the most revent (prev one)
In init: use hashmap
key: list of (value, timestamp)
- since timestamps are already called in increasing order, no need to sort, can use binary search to reduce get time complexity

Set():
- store the key : (value, timestamp pair to the END of the list)

Get():
- binary search the list attached to the key specified
"""