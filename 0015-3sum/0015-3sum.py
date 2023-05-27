class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for x in range(0, len(nums) - 1):
            if (x > 0 and nums[x] == nums[x-1]):
                continue
            l = x + 1
            h = len(nums) - 1
            while (l < h):
                sum = nums[l] + nums[h]
                if (sum + nums[x] == 0):
                    answer.append([nums[x], nums[l], nums[h]])
                    while (l < h and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < h and nums[h] == nums[h - 1]):
                        h -= 1
                    l += 1
                    h -= 1
                elif (sum + nums[x] > 0):
                    h -= 1
                else:
                    l += 1
        
        return answer