'''
DESCRIPTION:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''


class Solution:
    def twoSum(self, nums, target):
        dct = {}

        for ind, num in enumerate(nums):
            difference = target - num
            if difference in dct and dct[difference] != ind:
                return [dct[difference], ind]
            dct[num] = ind


if __name__ == '__main__':
    num_lst = Solution()
    print(num_lst.twoSum([3, 2, 3], 6))
    print(num_lst.twoSum([2, 7, 11, 15], 9))
    print(num_lst.twoSum([1, 0, 3, 8], 9))
    print(num_lst.twoSum([1, 5, 5, 5, 4], 10))
    print(num_lst.twoSum([7, 7], 14))