from typing import List
from functools import cache


'''
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
All the elements of nums are unique.

Follow up: What if negative numbers are allowed in the given array? 
How does it change the problem? 
What limitation we need to add to the question to allow negative numbers?
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(n=0):
            # base case
            if n >= target:
                return n == target

            result = 0
            for num in nums:
                result += dp(num + n)
            return result
        return dp()


sol = Solution()
print(sol.combinationSum4(nums=[1, 2, 3], target=4))
print(sol.combinationSum4(nums=[3, 1, 2, 4], target=4))
print(sol.combinationSum4(nums=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], target=10))
print(sol.combinationSum4(nums=[9], target=3))