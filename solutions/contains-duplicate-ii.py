class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # Dictionary to store number and its latest index
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True  # Found duplicate within range
            seen[num] = i  # Update latest index
        
        return False