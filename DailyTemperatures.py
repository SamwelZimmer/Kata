"""
DailyTemperatures.py

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # initialise an empty results array of zeros
        res = [0] * len(temperatures)
            
        # init empty stack. Each value will hold temp and an index
        stack = []
        
        # loop through each temp value
        for i, temp in enumerate(temperatures):
            
            # continue to iterate when next value greater than last
            while stack and temp > stack[-1][0]:
                
                # get temp and position of removed item
                stackTemp, stackIdx = stack.pop()
                
                # add number of days into results array at index
                res[stackIdx] = (i - stackIdx)
            
            # add current value to stack
            stack.append([temp, i])
            
        return res
            
        
        
        
sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))