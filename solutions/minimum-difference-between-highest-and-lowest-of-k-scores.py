class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        res,score=float('inf'),0
        if(len(nums)==1):
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                score = max(nums[i],nums[j])-min(nums[i],nums[j])
                res = min(res,score)
        return res