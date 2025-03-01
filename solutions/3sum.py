class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input to make it easier to avoid duplicates
        sol = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the i-th element
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    sol.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:  # Skip duplicates for the j-th element
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:  # Skip duplicates for the k-th element
                        k -= 1
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        
        return sol