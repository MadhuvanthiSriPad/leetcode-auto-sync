class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,n
        if(m+n==n):
            for i in range(m+n):
                nums1[i]=nums2[i]
        else:
            while(j<=(m+n)-1 and i<=n-1):
                nums1[j] =nums2[i]
                j+=1
                i+=1
        nums1=nums1.sort()