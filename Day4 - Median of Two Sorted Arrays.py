# level -1  O((m+n)log(m+n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()
        return nums1[len(nums1)/2] if len(nums1) & 1 else (nums1[len(nums1)/2] + nums1[len(nums1)/2-1])/2.

# level 0  O(n+m)

class Solution(object):
    def merge(self, nums1, nums2):
        res = []
        while len(nums1) and len(nums2):
            if nums1[0] > nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))
        if len(nums1):
            res.extend(nums1)
        else:
            res.extend(nums2)
        return res

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = self.merge(nums1, nums2)
        return nums1[len(nums1)/2] if len(nums1) & 1 else (nums1[len(nums1)/2] + nums1[len(nums1)/2-1])/2.

# level 1  O(log(n+m))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
