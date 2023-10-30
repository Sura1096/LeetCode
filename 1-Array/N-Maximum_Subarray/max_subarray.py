from typing import List

'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''


# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        cur_sum = 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            maxi = max(cur_sum, maxi)

        return maxi


sol = Solution()
print(sol.maxSubArray([-2, -1]))


# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# [5, 4, -1, 7, 8]
# [-1]
# [-1, -2]


# Divide and conquer
# class Solution:
#     def maxSubArray(self, nums: List[int]):
#         def maxSubArray(nums):
#             if len(nums) == 1:
#                 return nums[0]
#
#             mid = len(nums) // 2
#             left = maxSubArray(nums[:mid])
#             right = maxSubArray(nums[mid:])
#
#             left_sum = float('-inf')
#             summ = 0
#             for i in range(mid-1, -1, -1):
#                 summ += nums[i]
#                 left_sum = max(summ, left_sum)
#
#             right_sum = float('-inf')
#             summ = 0
#             for i in range(mid, len(nums)):
#                 summ += nums[i]
#                 right_sum = max(summ, right_sum)
#
#             cross = left_sum + right_sum
#
#             return max(left, right, cross)
#
#         return maxSubArray(nums)
#
#
# sol = Solution()
# print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
