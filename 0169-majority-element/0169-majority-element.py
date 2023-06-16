class Solution:
    def counter(self, target: int, s: int, e: int, nums:List[int]) -> int:
        count = 0
        for i in range(s, e+1):
            if nums[i] == target:
                count += 1
        return count
    def majorityElement(self, nums: List[int]) -> int:
        def recur(s, e):
            nonlocal nums
            if s == e:
                return nums[s]
            m = (s + e)//2
            l = recur(s, m)
            r = recur(m+1, e)
            if l == r:
                return l
            else:
                if self.counter(l, s, e, nums) > self.counter(r, s, e, nums):
                    return l
                return r
        return recur(0, len(nums) - 1)