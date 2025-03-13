class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        maxi = 0
        i = 0
        j = 0
        flag = 0

        while j < n:
            if flag == 0:
                if nums[j] % 2 == 0 and nums[j] <= threshold:
                    i = j
                    maxi = max(maxi, j - i + 1)
                    flag = 1
            elif flag == 1:
                x = nums[j - 1]
                y = nums[j]
                c = x + y
                if c % 2 and nums[j] <= threshold:
                    maxi = max(maxi, j - i + 1)
                else:
                    flag = 0
                    j -= 1
            j += 1

        return maxi