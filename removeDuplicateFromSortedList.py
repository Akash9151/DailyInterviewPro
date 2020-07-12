#Given a sorted list of size n, with m unique elements (thus m < n), modify the list such that the first m unique elements in the list will be sorted, ignoring the rest of the list. Your solution should have a space complexity of O(1). Instead of returning the list (since you are just modifying the original list), you should return what m is.#



def remove_dups(nums):
    store = None
    rm = []
    for i in nums:
        if( store == i ):
            rm.append(i)
        else:
            store= i
    for i in rm:
        nums.remove(i)
    return len(nums)


nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1