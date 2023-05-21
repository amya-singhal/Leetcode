class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def recur(target):
            l = 0
            h = len(nums) - 1
            while (l <= h):
                mid = l + (h - l) // 2
                if (nums[mid] < target):
                    l = mid + 1
                else:
                    h = mid - 1
            return l
        l = recur(target)
        h = recur(target+1) - 1
        if (l <= h):
            return [l, h]
        else:
            return [-1,-1]
                    