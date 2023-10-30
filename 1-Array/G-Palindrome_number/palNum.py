class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == (str(x))[::-1]


n = Solution()
print(n.isPalindrome(1981))