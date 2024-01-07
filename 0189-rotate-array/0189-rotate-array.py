class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if (n == k):
            return
        k = k%n
        nums.reverse()
        for i in range(0, k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range(k, (n+k)//2):
            nums[i], nums[n-1-i+k] = nums[n-1-i+k], nums[i]
        return
        