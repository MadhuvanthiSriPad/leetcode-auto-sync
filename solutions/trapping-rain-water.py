class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL, maxR , minLR ,res = [0]*n , [0]*n , [0]*n, 0

        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):  
            maxR[i] = max(maxR[i + 1], height[i + 1])
        
        for i in range(len(height)):
            minLR[i]=(min(maxL[i],maxR[i]))


        for i in range(len(height)):
            if (minLR[i] - height[i])<0:
                res+=0
            else:
                res+= minLR[i] - height[i]
        return res