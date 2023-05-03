class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = []
        def exists(num, list):
            for i in list:
                if i == num:
                    return True
            return False
        t1 = []
        t2 = []
        for n in nums1:
            if (not exists(n, nums2) and not exists(n, t1)):
                t1.append(n)
        answer.append(t1)
        for n in nums2:
            if (not exists(n, nums1) and not exists(n, t2)):
                t2.append(n)
        answer.append(t2)
        return answer
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        