from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int):
#         left, right = 0, len(nums) - 1
#         if val in nums:
#             while left <= right:
#                 if nums[left] == val and nums[right] != val:
#                     nums[left] = nums[right]
#                     left += 1
#                     right -= 1
#                 elif nums[left] == val and nums[right] == val:
#                     right -= 1
#                 elif nums[left] != val and nums[right] == val:
#                     left += 1
#                     right -= 1
#                 else:
#                     left += 1
#
#             return left
#
#
# array = Solution()
# print(array.removeElement([2], 2))

# 1, 1, 1, 2, 3, 4, 5, 1, 1, 4, 7, 8, 1, 1
# 0,1,2,2,3,0,4,2


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         left = 0
#         right = len(nums) - 1
#
#         count = 0
#         while left <= right:
#             if nums[left] == val and nums[right] != val:
#                 nums[left] = nums[right]
#                 left += 1
#                 right -= 1
#                 count += 1
#             elif nums[left] == val and nums[right] == val:
#                 right -= 1
#             else:
#                 left += 1
#                 count += 1
#
#         return count


class Solution:
    def removeElement(self, nums: List[int], val: int):
        left, right = 0, len(nums) - 1
        if val in nums:
            while left <= right:
                if nums[left] == val:
                    if nums[right] != val:
                        nums[left] = nums[right]
                        left += 1
                        right -= 1
                    elif nums[right] == val:
                        right -= 1
                elif nums[left] != val:
                    if nums[right] == val:
                        left += 1
                        right -= 1
                    elif nums[right] != val:
                        left += 1

            return left


array = Solution()
print(array.removeElement([1, 1, 1, 2, 3, 4, 5, 1, 1, 4, 7, 8, 1, 1], 1))