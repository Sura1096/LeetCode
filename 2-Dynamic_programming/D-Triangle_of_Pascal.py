from typing import List


'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            triangle = [[1], [1, 1]] + [[1]] * (numRows - 2)

            for i in range(2, numRows):
                for j in range(1, i):
                    triangle[i] = triangle[i] + [triangle[i-1][j] + triangle[i-1][j-1]]
                triangle[i] = triangle[i] + [1]

            return triangle


sol = Solution()
print(sol.generate(5))