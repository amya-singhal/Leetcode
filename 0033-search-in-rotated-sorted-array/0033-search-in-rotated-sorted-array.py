class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [2,4,5,6,7,0,1], 0
        [4,5,6,7,0,1,2]
        [5,6,7,0,1,2,4]
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1