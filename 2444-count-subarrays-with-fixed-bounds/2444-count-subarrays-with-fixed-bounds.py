class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        [1,3,5,2,7,5]
        l = 1
        min = T
        max = T
        ans 1
        """
        ans = 0
        left, right, start = -1,-1,-1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
            if nums[i] == minK:
                left = i
            if nums[i] == maxK:
                right = i
            ans += max(0, min(left, right)-start)
        return ans