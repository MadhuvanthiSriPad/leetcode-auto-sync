class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)  # Step 1: Count occurrences
        max_length = 0
        best_pair = None

        # Step 2: Find the best (num, num+1) pair
        for num in freq:
            if num + 1 in freq:  # Check for a harmonious pair
                total_length = freq[num] + freq[num + 1]
                if total_length > max_length:
                    max_length = total_length
                    best_pair = (num, num + 1)

        if best_pair is None:
            return 0  # No valid harmonious subsequence exists

        # Step 3: Extract subsequence while preserving order
        result = [x for x in nums if x in best_pair]
        return len(result)