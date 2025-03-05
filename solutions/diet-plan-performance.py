class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pts = 0
        wind_sum = sum(calories[:k])

        if(wind_sum<lower):
            pts-=1
        elif(wind_sum>upper):
            pts+=1
        for i in range(k,len(calories)):
            wind_sum += calories[i]-calories[i-k]

            if(wind_sum<lower):
                pts-=1
            elif(wind_sum>upper):
                pts+=1 
        return pts