class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        t = l1 + l2
        half = t//2
        if l2 < l1:
            nums1, nums2 = nums2, nums1
        # binary search on smaller array, nums1
        l = 0
        r = len(nums1)-1
        while(True):
            i = (l+r)//2
            j = half - i - 2
            
            left1 = nums1[i] if i >= 0 else float("-inf")
            right1 = nums1[i+1] if i+1 < len(nums1) else float("inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right2 = nums2[j+1] if j+1 < len(nums2) else float("inf")
            
            if right1 >= left2 and right2 >= left1:
                if t % 2 == 0:
                    return (max(left1,left2) + min(right1,right2)) / 2
                else:
                    return min(right1, right2)
            elif right1 < left2:
                l = i + 1
            else:
                r = r - 1
            
                