"""
- design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain time stamp. 

- implement TimeMap class

"""
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key: list of (timestamp, value) pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        if not entries:
            return ""
        
        # Binary search to find the largest timestamp <= target
        left, right = 0, len(entries) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            current_ts, current_val = entries[mid]
            
            if current_ts == timestamp:
                return current_val
            elif current_ts < timestamp:
                result = current_val  # potential candidate
                left = mid + 1
            else:
                right = mid - 1
                
        return result


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)