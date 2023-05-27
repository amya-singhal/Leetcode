class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums) - 1):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            l = i + 1
            h = len(nums) - 1
            x = -nums[i]
            while(l < h):
                sum = nums[l] + nums[h]
                if (sum == x):
                    tmp = [nums[i], nums[l], nums[h]]
                    if tmp not in ans:
                        ans.append(tmp)
                    l += 1
                    h -= 1
                elif (sum > x):
                    h -= 1
                else:
                    l += 1
        return ans
        