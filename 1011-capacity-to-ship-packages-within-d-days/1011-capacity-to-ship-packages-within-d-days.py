class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high=sum(weights)
        ans=-1
        while low <=high:
            capacity=low + ((high-low)//2) 
            day=1
            current_load=0
            for j in weights:
                if current_load+j > capacity:
                    day+=1
                    current_load= j 
                    if day > days:
                        break 
                elif current_load+j <= capacity:
                    current_load+=j
            if day <=days:
                ans=capacity
                high= capacity-1
            else:
                low=capacity+1
        return ans