class Solution(object):
    def dailyTemperatures(self,temperatures):
        result = [0]*len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT,stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t,i])
        return result
        