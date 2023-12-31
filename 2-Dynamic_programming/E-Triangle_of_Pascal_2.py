from typing import List


'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            triangle = [[1], [1, 1]] + [[1]] * (rowIndex - 1)

            for i in range(2, rowIndex+1):
                for j in range(1, i):
                    triangle[i] = triangle[i] + [triangle[i-1][j] + triangle[i-1][j-1]]
                triangle[i] = triangle[i] + [1]
            return triangle[-1]


sol = Solution()
print(sol.getRow(3))