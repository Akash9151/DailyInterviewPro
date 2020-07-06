
# Given an array of heights, determine whether the array forms a "mountain" pattern. A mountain pattern goes up and then down.

# Like

#   /\
#  /  \
# /    \

class Solution(object):
  def validMountainArray(self, arr):
    if(len(arr) % 2 == 0):
        return False
    else:
        count = 0
        n = len(arr) // 2
        for i in range(n + 1):
            if(arr[n - i] == arr[n + i]):
                count += 1
            else:
                return False
        if(count == (n + 1)):
            return True
        
        

print(Solution().validMountainArray([1, 2, 3, 2, 1]))
# True

print(Solution().validMountainArray([1, 2, 3]))
# False
