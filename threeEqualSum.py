
# Given an array of numbers, determine whether it can be partitioned into 3 arrays of equal sums.

# For instance,
# [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1] can be partitioned into:
# [0, 2, 1], [-6, 6, -7, 9, 1], [2, 0, 1] all of which sum to 3.

class Solution(object):
    def canThreePartsEqualSum(self, A):
        count = 0
        for i in A:
            count += i
        if(count % 3 == 0):
            num = count // 3
            list1 = []
            list2 = []
            list3 = []
            list1V = True;
            list2V = True;
            list3V = True;
            sum = 0
            for i in A:
                if(list1V):
                    sum += i
                    if(sum != num):
                        list1.append(i)
                    else:
                        list1.append(i)
                        list1V = False
                        sum = 0
                elif (list2V):
                    sum += i
                    if(sum != num):
                        list2.append(i)
                    else:
                        list2.append(i)
                        list2V = False
                        sum = 0
                else:
                    sum += i
                    if(sum != num):
                        list3.append(i)
                    else:
                        list3.append(i)
                        list3V = False
                        return True
            if(sum != num):
                return False
        return False
      # Fill this in.0

print(Solution().canThreePartsEqualSum(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    
print(Solution().canThreePartsEqualSum(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1, 3, 6]))
# True
