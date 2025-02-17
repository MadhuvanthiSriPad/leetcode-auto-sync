class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if (nums[i]<nums[j]<nums[k]):
                        return True
        return False
        