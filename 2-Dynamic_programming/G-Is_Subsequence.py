'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        seq = ''

        for i in range(len(s)):
            for j in range(pointer, len(t)):
                if s[i] == t[j]:
                    seq += t[j]
                    pointer = j + 1
                    break
        if seq == s:
            return True
        return False


sol = Solution()
print(sol.isSubsequence(s='abc', t='ahbgdc'))
print(sol.isSubsequence(s='aec', t='abcde'))
print(sol.isSubsequence(s='a', t='e'))
print(sol.isSubsequence(s='a', t=''))
print(sol.isSubsequence(s='ab', t='baab'))
print(sol.isSubsequence(s='axc', t='abcde'))
print(sol.isSubsequence(s='aaaaaa', t='bbaaaa'))