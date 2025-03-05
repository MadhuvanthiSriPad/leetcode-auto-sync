class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm={}

        for i in range(len(nums)):
            if nums[i] in hm:
                return True
            if(i>=k):
                hm.pop(nums[i-k],None)
            hm[nums[i]] = hm.get(nums[i],0)+1
        return False