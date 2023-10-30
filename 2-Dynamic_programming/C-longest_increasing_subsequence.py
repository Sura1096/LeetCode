from typing import List


'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence 

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(target, dp):
            left = 0
            right = len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                ind = binarySearch(nums[i], dp)
                dp[ind] = nums[i]
        return len(dp)


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(sol.lengthOfLIS([0, 100, 0, 1, 50, 20, 55, 65, 30, 80, 60, 1000, 66]))
print(sol.lengthOfLIS([3, 1, 2]))
print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))