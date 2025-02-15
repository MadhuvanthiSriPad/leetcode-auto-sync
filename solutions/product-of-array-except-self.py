class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[1]*len(nums)
        rp,lp=1,1

        for i in range(len(nums)):
            res[i]*=lp
            lp*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=rp
            rp*=nums[i]
        return res
        