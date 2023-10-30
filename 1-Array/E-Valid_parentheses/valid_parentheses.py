# def isValid(s):
#     stack = []
#     flag = True
#
#     for char in s:
#         if char in "([{":
#             stack.append(char)
#         elif char in ")]}":
#             if len(stack) == 0:
#                 flag = False
#                 break
#             front = stack.pop()
#
#             if front == '(' and char == ')':
#                 continue
#             elif front == '[' and char == ']':
#                 continue
#             elif front == '{' and char == '}':
#                 continue
#             flag = False
#             break
#
#     if flag is True and len(stack) == 0:
#         return True
#     return False
#
#
# print(isValid('(]'))


class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char in '([{':
                stack.append(char)
            elif stack and char in ')]}':
                last = stack.pop()

                if last == '(' and char == ')':
                    continue
                elif last == '[' and char == ']':
                    continue
                elif last == '{' and char == '}':
                    continue
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True


par = Solution()
print(par.isValid('}'))