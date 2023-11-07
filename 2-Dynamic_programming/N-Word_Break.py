from typing import List

'''
139. Word Break

Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = dp[i] or dp[j + 1]

        return dp[-1]


sol = Solution()
print(sol.wordBreak(s='leetcode', wordDict=["leet", "code"]))
print(sol.wordBreak(s='applepenapple', wordDict=["apple", "pen"]))
print(sol.wordBreak(s='catsandog', wordDict=["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak(s='cars', wordDict=["car", "ca", "rs"]))
print(sol.wordBreak(s='bb', wordDict=["a", "b", "bbb", "bbbb"]))
print(sol.wordBreak(s='aaaaaaa', wordDict=["aaaa", "aaa"]))
print(sol.wordBreak(s='a', wordDict=["b"]))
print(sol.wordBreak(s='abcd', wordDict=["a", "abc", "b", "cd"]))