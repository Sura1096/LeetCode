import random

# def two_sum(array, target):
#    for ind in range(len(array)-1):
#        if array[ind]+array[ind+1] == target:
#            return [ind, ind+1]

# array = []
# for i in range(10):
#    array.append(random.randint(1, 10))
# print(array)
#
# target = random.randint(1, 10)
# print(target)
# print(two_sum(array, target))


#IDK HOW IT WORKS
#def two_sum(arr,targ):
#    look_for = {}
#    for n,x in enumerate(arr):
#        try:
#            return look_for[x], n
#        except KeyError:
#            look_for.setdefault(targ - x,n)

#a = [2,7,1,15]
#t = 9
#print(two_sum(a,t))


# def TwoSum(nums: list[int], target: int) -> list[int] | bool:
#     for ind in range(len(nums)):
#         if ind + 1 < len(nums) and nums[ind] + nums[ind + 1] == target:
#             return [ind, ind+1]
#     return False


# arr = [5, 9, 4, 2, 1, 7]
# t = 8
# print(TwoSum(arr, t))


# def twoSum(nums: list[int], target: int) -> list[int]:
#     ind = 0
#     flag = True
#     while flag:
#         num = target - nums[ind]
#         if num in nums and ind != nums.index(num):
#             flag = False
#             if ind < nums.index(num):
#                 return [ind, nums.index(num)]
#             elif ind > nums.index(num):
#                 return [nums.index(num), ind]
#         else:
#             ind += 1
#
#
# n = [2, 7, 11, 15]
# t = 9
# print(twoSum(n, t))


def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap and i != hashmap[complement]:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


a = [5, 3, 4, 2, 1, 7]
t = 15
print(two_sum(a, t))