class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        try:
            n, m = len(matrix), len(matrix[0])
        except IndexError:
            return 0
        heights = [0] * m
        res = 0
        
        for i in xrange(n):
            for j in range(m):
                heights[j] = heights[j]+1 if matrix[i][j] == '1' else 0
            heights.append(-1)
            
            stack = []
            for j in xrange(m+1):
                while stack and heights[j] < heights[stack[-1]]:
                    height_index = stack.pop()
                    h = heights[height_index]
                    if len(stack) == 0:
                        w = j
                        res = max(res, w*h)
                    else:
                        w = j - 1 - stack[-1]
                        res = max(res, w*h)
                stack.append(j)
        return res
