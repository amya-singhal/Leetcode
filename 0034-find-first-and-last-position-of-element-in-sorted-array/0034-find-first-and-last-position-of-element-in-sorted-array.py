class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def recur(target):
            l = 0
            r = len(nums) - 1
            while(l <= r):
                m = (l+r)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        left = recur(target)
        right = recur(target+1) - 1
        if (left <= right):
            return [left, right]
        else:
            return [-1,-1]