class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in range(len(nums)):
            if nums[i]==k:
                cnt+=1
                break
            s=0
            s+=nums[i]
            for j in range(i+1,len(nums)):
                if(s+nums[j]==k):
                    cnt+=1
                    break
                s+=nums[j]
        return cnt