class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxL = float('-inf')  # To handle negative numbers
        for left in range(len(nums) - k + 1):  # Ensuring the window is within bounds
            wind_sum = sum(nums[left:left + k])  # Compute sum for each window
            maxL = max(maxL, wind_sum)  # Update max sum
            print(left, left + k, wind_sum)  # Debugging output
        
        return maxL / k 