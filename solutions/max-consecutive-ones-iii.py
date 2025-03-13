class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res=0
        i=0
        zero = 0
        for right in range(len(nums)):
            if(nums[right]==0):
                zero+=1

            while(zero>k):
                if(nums[i]==0):
                    zero-=1
                i+=1
            res = max(res,right-i+1)
        return res