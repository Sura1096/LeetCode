from typing import List

'''
152. Maximum Product Subarray

Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = float('-inf')
        product = 1
        for ind in range(len(nums)):
            product *= nums[ind]
            maxi = max(product, maxi)
            if product == 0:
                product = 1

        product = 1
        for ind in range(len(nums) - 1, -1, -1):
            product *= nums[ind]
            maxi = max(maxi, product)
            if product == 0:
                product = 1

        return maxi


sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, -1, -3, 2, 5]))
print(sol.maxProduct([-3, -1, -1]))
print(sol.maxProduct([-1, -2, -3, 0]))
print(sol.maxProduct([-2, 0, -1]))
print(sol.maxProduct([-2, -3, -1, -3, 4, 5]))
print(sol.maxProduct([-2, 0, -1, 2, 3, 4]))
print(sol.maxProduct([-3, 0, 1, -2]))
print(sol.maxProduct([-2]))
