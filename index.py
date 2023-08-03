def two_sum(nums, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

    # If no solution found, return an empty list or raise an exception, depending on your use case
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
