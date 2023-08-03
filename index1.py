def two_sum(nums, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

    # If no solution found, return an empty list or raise an exception, depending on your use case
    return []

# Example usage:
nums = [3, 2, 4]
target = 6
result = two_sum(nums, target)
print(result)  # Output: [1, 2]
