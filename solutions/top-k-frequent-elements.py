class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        unique = Counter(nums)
        res=[]
        max_heap = [key for key,val in unique.items()]
        heapq.heapify(max_heap)

        while k:
            res.append(heapq.heappop(max_heap))
            k-=1
        
        return res