class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxFreq = 0
        for i in count:
            if(i+1 in count):
                maxFreq = max(maxFreq,count[i]+count[i+1])
        return maxFreq                                                                                                                                                                                                                                                                                                                                                                            