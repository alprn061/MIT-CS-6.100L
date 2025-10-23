'''136. Single Number
Easy
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
def singleNumber(nums: list[int]) -> int:
    seen = []
    for i in nums:
        # 2,2,1
        if i not in seen:
            seen.append(i)
        elif i in seen:
            seen.remove(i)
    return seen[0]
#print(singleNumber([2,2,1])) # outpu :1
#print(singleNumber([4,1,2,1,2])) # output : 4
#print(singleNumber([1])) # output : 1
# runtime:628ms, memory:19.52mb








'''350. Intersection of Two Arrays II
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    inters = []
    for i in nums1:
        if i in nums2:
            inters.append(i)
            nums2.remove(i)
    return inters

#print(intersect([1,2,2,1],[2,2])) # Output: [2,2]
#print(intersect([4,9,5],[9,4,9,8,4])) # Output: [4,9]
#print(intersect([1,2,2,1],[2])) # Output: [2]
#print(intersect(nums1 = [1], nums2 = [9,4,8,4])) # Output: []

# runtime : 11ms, memory : 18.01 mb





'''58. Length of Last Word
Easy
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
def lengthOfLastWord(s: str) -> int:
    a = s.strip().split(" ")
    return len(a[-1])

#print(lengthOfLastWord("Hello World")) # Output: 5
#print(lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
#print(lengthOfLastWord("luffy is still joyboy")) # Output: 6

# runtime : 0ms, memory :18.00 mb


