nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

# First way
i = 0
j = 1

while i <= j != len(nums):
    if nums[i] != nums[j]:
        nums[i + 1] = nums[j]
        i += 1
    j += 1

print(i + 1)


# Second way
nums[:] = list(sorted(set(nums)))
print(len(nums))