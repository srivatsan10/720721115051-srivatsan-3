
def binary_search(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    middle = (left + right) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] < target:
      left = middle + 1
    else:
      right = middle - 1
  return -1
nums = [1, 3, 5, 6]
target = 5
target_val = 2
target_value = 7
result = binary_search(nums, target)
result1 = binary_search(nums,target_val)
result2 = binary_search(nums,target_value)
print(result)
print(result1)
print(result2)
