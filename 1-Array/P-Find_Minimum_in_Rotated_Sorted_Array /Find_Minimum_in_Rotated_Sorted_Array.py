from typing import List

'''
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

'''


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#
#         mid = len(nums) // 2
#         left = min(nums[0], self.findMin(nums[:mid]))
#         right = min(nums[0], self.findMin(nums[mid:]))
#
#         return min(left, right)
#
#
# sol = Solution()
# print(sol.findMin([3, 4, 5, 1, 2]))
# print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
# print(sol.findMin([11, 13, 15, 17]))
# print(sol.findMin([5, 10, 15, 17, 18, 30, 31, 35]))
# print(sol.findMin([3, 1, 2]))
# print(sol.findMin([5, 1, 2, 3, 4]))


# Another way
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[0]
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            mid = (low + high) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res


sol = Solution2()
print(sol.findMin([3, 4, 5, 1, 2]))
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin([11, 13, 15, 17]))
print(sol.findMin([5, 10, 15, 17, 18, 30, 31, 35]))
print(sol.findMin([3, 1, 2]))
print(sol.findMin([5, 1, 2, 3, 4]))