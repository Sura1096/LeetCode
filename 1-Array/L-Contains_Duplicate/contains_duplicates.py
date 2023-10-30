from typing import List


'''
217. Contains Duplicate

DESCRIPTION:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        set_nums = set()

        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                return True

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicates([1, 2, 3, 1]))
    print(sol.containsDuplicates([1, 2, 3, 4]))
    print(sol.containsDuplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))