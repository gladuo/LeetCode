# level 1  O(n*size(integer))

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

# level 2  O(n)

# solution 1:
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        gate = 1  # pow2 gate
        for i in range(1, num+1):
            if i == gate:
                gate <<= 1
                rec = 1
            else:
                rec = 1 + res[i-gate]
            res.append(rec)
        return res

# solution 2:
# a more direct implementation
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num+1):
            res.append(res[i>>1]+(i&1))
        return res
