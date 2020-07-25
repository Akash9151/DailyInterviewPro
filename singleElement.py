class Solution(object):
  def findSingle(self, nums):
    # Sort Array

    nums.sort()
    
    count = 1

    # Find Single Element
    for i in range(1, len(nums)):
        if(nums[count-1] == nums[count]):
            count += 2
            continue

        else:
            return nums[count-1]

nums = [7, 3, 5, 5, 4, 3, 4, 8, 8]
print(Solution().findSingle(nums))
# 7
