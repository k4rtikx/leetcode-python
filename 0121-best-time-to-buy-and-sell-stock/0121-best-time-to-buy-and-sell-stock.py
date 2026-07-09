class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        if len(prices)==0 or len(prices)==1:
            print(0)
        for i in range(1,len(prices)):
            buy=min(buy,prices[i])
            #print(buy)
            sell=max(sell,prices[i]-buy)
            #print(sell)
        return sell
        