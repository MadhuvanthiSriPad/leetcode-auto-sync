class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        print(window)
        med = []

        for i in range(k,len(nums)+1):
            if(k%2==0):
                mid = k//2
                med.append((window[mid]+window[mid-1])/2)
            else:
                med.append(window[k//2])
            if(i<len(nums)):
                window.remove(nums[i-k])
                window.add(nums[i])

        return med