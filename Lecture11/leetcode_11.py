'''448. Find All Numbers Disappeared in an Array
Easy
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
'''
# SOLUTION FROM AI
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for num in nums:
        i = abs(num) - 1
        if nums[i] > 0:
            nums[i] = -nums[i]
    return [i + 1 for i in range(len(nums)) if nums[i] >0]

#print(findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])) # Output: [5,6]
#print(findDisappearedNumbers(nums = [1,1])) # Output: [2]






'''283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
'''
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for num in nums:
        if num ==0:
            nums.remove(num)
            nums.append(num)
    print(nums)

print(moveZeroes(nums = [0,1,0,3,12])) # Output: [1,3,12,0,0]
print(moveZeroes(nums = [0])) # Output: [0]
