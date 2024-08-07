class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search for the pivot
        l, r = 0, len(nums)-1
        while (l <= r):
            m = l+(r-l)//2
            # print(l,r,m)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[m] >= target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[r] >= target >= nums[m]:
                    l = m+1
                else:
                    r = m-1
        return -1 