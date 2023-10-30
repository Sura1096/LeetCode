from typing import List


'''
238. Product of Array Except Self

DESCRIPTION:
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # First way with time and memory complexity O(n)
        # n = len(nums)
        # left_product = [1] * n
        # right_product = [1] * n
        #
        # for i in range(1, n):
        #     left_product[i] = left_product[i - 1] * nums[i - 1]
        #
        # for i in range(n - 2, -1, -1):
        #     right_product[i] = right_product[i + 1] * nums[i + 1]
        #
        # result = [left_product[i] * right_product[i] for i in range(n)]
        #
        # for i in range(n):
        #     result.append(left_product[i] * right_product[i])
        #
        # print(left_product)
        # print(right_product)
        #
        # return result

        # Another way with time complexity O(n) and memory complexity O(1)
        result = [1] * len(nums)
        prefix = 1
        for ind, num in enumerate(nums):
            result[ind] = prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == '__main__':
    p = Solution()
    print(p.productExceptSelf([1, 2, 3, 4]))
    print(p.productExceptSelf([-1, 1, 0, -3, 3]))
    print(p.productExceptSelf([2, 3, 1, 4, 5]))
    print(p.productExceptSelf([0, 0]))


# EXPLANATION
# https://www.youtube.com/watch?v=RGQ1blF6P7s&ab_channel=%D0%A1%D1%83%D1%80%D0%B5%D0%BD%D0%A5%D0%BE%D1%80%D0%B5%D0%BD%D1%8F%D0%BD