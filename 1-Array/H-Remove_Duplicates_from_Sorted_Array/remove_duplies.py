from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        left = cur_ind = 0

        for i in range(len(nums)):
            if cur_ind < len(nums) and nums[left] != nums[cur_ind]:
                left += 1
                nums[left] = nums[cur_ind]
            cur_ind += 1

        return nums, left + 1


l = Solution()
print(l.removeDuplicates([0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4]))