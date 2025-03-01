class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        unique = Counter(nums)
        res=[]
        for key, val in unique.items():
            if (val>=k and len(res)<k):
                res.append(key)
        return res