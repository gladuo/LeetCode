# level 1

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, num+1):
            cnt = 0
            while i:
                if i & 1:
                    cnt += 1
                i = i >> 1
            res.append(cnt)
        return res
