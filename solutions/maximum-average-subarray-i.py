class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind_sum = sum(nums[:k])
        maxL=wind_sum
        print(wind_sum)
        
        for i in range(k,len(nums)):
            wind_sum += nums[i]-nums[i-k]
            maxL = max(maxL,wind_sum)
        return maxL / k 