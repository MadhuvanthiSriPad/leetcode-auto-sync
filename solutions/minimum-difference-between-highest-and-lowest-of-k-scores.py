class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = float('inf')
        if(len(nums)==1):
            return 0
        for i in range(len(nums)-k+1):
            res = min(res,nums[i+k-1]-nums[i])
        return res