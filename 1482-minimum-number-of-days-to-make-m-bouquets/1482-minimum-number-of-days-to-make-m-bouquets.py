class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high= max(bloomDay)
        answer=-1
        while low <=high:
            # mid find no of days
            mid=low + ((high-low)//2)
            bouquets=0
            count=0
            for i in range (len(bloomDay)):
                if bloomDay[i] <=mid:
                    count+=1
                    if count==k:
                        bouquets+=1
                        count=0
                else:
                    count=0
            if bouquets>=m:
                answer =mid
                high= mid-1
            else:
                low=mid+1
        return answer
