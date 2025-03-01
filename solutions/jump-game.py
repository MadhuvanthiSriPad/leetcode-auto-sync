class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n  # DP array to track if we can reach the last index
        dp[-1] = True  # The last index is always reachable from itself

        for i in range(n - 2, -1, -1):  # Traverse backwards
            max_jump = min(i + nums[i], n - 1)  # Don't jump beyond the last index
            for j in range(i + 1, max_jump + 1):  # Check if any reachable index is True
                if dp[j]:  # If we can reach `j` and `j` can reach the last index
                    dp[i] = True
                    break  # No need to check further
                
        return dp[0] 