class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        number = nums[0]
        for n in nums[1:]:
            if n != number:
                if count == 0:
                    number = n
                    count += 1
                else:
                    count -= 1
            else:
                count += 1
        return number