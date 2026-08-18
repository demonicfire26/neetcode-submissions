class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies of each number
        key = Counter(nums)
        
        result = [num for num, count in key.most_common(k)]

        return result
