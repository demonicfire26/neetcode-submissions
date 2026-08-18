class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        Use a dictionary where each key maps to a list of [timestamp, value] pairs.
        """
        self.store = {}  # key -> list of [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with value at the given timestamp.
        Assumes timestamps are strictly increasing for each key.
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the value with the largest timestamp_prev <= timestamp.
        If no such value exists, returns "".
        Uses binary search since timestamps are sorted.
        """
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""
        
        # Binary search for the largest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]  # Update result with this valid value
                left = mid + 1  # Try to find a larger valid timestamp
            else:
                right = mid - 1
                
        return result


