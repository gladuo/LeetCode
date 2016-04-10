class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(1)
            elif stack[-1] & 1:
                last = stack.pop()
                stack[-1] += last + 1
            else:
                stack.append(0)
        return max(sub for sub in stack) / 2 * 2
