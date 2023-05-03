class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = []
        t1 = []
        t2 = []
        t1 = set(nums1) - set(nums2)
        t2 = set(nums2) - set(nums1)
        answer.append(t1)
        answer.append(t2)
        return answer
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        