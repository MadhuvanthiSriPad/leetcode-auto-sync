class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i, j = -1, len(nums)-k
        result = []
        while j >= 0:
            heapq.heappush(result, (nums[i] - nums[j]))
            i -= 1
            j -= 1
        return result[0]