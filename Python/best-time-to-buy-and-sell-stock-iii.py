# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. 
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
#

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return self.maxKPairsProfit(prices, 2)
    
    def maxKPairsProfit(self, prices, k):
        k_sum = [float("-inf") for _ in xrange(2 * k)]
        for i in xrange(len(prices)):
            pre_k_sum = list(k_sum)
            j, sign = 0, -1
            while j < len(k_sum) and j <= i:
                diff = sign * prices[i]
                
                if j > 0:
                    diff += pre_k_sum[j - 1]
                
                k_sum[j] = max(diff, pre_k_sum[j])
                j += 1
                sign *= -1
                
        return k_sum[-1]
    
class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)
            
        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right, max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)
            
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profits_from_left[i] + max_profits_from_right[i])
        
        return max_profit
        
if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print result
