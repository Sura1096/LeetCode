# strs = ['paparazzi', 'paparazi', 'paparazzi']
# prefix = strs[0]
#
# for i in range(1, len(strs)):
#     j = 0
#     new_prefix = ''
#     for char in strs[i]:
#         if j < len(prefix) and prefix[j] == char:
#             new_prefix += char
#         else:
#             break
#         j += 1
#     prefix = new_prefix
#
# print(prefix)




class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            new_prefix = ''
            for char in strs[i]:
                if j < len(prefix) and prefix[j] == char:
                    new_prefix += char
                    j += 1
                else:
                    break
            prefix = new_prefix

        return prefix


w = Solution()
print(w.longestCommonPrefix(['paparazzi', 'paparazi', 'paparazzi']))
