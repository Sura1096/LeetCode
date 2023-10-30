from typing import List


'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for fix in range(len(nums) - 2):
            if nums[fix] > 0:
                break
            if fix > 0 and nums[fix] == nums[fix - 1]:
                continue
            left = fix + 1
            right = len(nums) - 1

            while left < right:
                total = nums[fix] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplet = [nums[fix], nums[left], nums[right]]
                    answer.append(triplet)
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                    while left < right and nums[right] == triplet[2]:
                        right -= 1
        return answer


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 0, 0]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([-5, 1, 0, 6, 5, -1, 3, 8, -8]))