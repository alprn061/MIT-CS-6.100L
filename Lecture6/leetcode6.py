'''28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''
# runtime 0ms
def strStr(haystack, needle):  #easy
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    temp = ""
    #check if needle is in haystack or not
    if needle in haystack:
        # clarify the position of needle
        return haystack.index(needle)
    else:
        return -1
    
# solution from community 
def strStr2(haystack, needle):
    # makes sure we don't iterate through a substring that is shorter than needle
    for i in range(len(haystack) - len(needle) + 1):
        # check if any substring of haystack with the same length as needle is equal to needle
        if haystack[i : i+len(needle)] == needle:
            # if yes, we return the first index of that substring
            return i
    # if we exit the loop, return -1        
    return -1
print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("burrr", "rr"))
print(strStr2("sadbutsad", "sad"))
print(strStr2("leetcode", "leeto"))
print(strStr2("burrr", "rr"))
print("--------------------------------------------")




'''34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
# runtime 0ms, memory 13.20mb
def searchRange(nums, target): #medium
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # check if target in nums
    if target in nums:
        #find first occurence of target
        first = nums.index(target)
        # remove the first occurence
        nums.remove(target)
        # chechk again if target in nums
        if target in nums:
            # find last occurence of target and find it index
            second = len(nums) - nums[::-1].index(target)
            return [first, second]
        else:
            # if there is one occurence of target return just first
            return[first,first]
    # if target not in nums return [-1,-1]
    else:
        return [-1,-1]

print(searchRange([5,7,7,9,8,9,10], 9))
print(searchRange([5,7,7,8,8,10], 5))
print(searchRange([1], 1))
print(searchRange([3,3,3], 3))


''' Very nice solution for 34 from community

def searchRange(nums: List[int], target: int) -> List[int]:

    def search(x):
        lo, hi = 0, len(nums)           
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid+1
            else:
                hi = mid                    
        return lo
        
    lo = search(target)
    hi = search(target+1)-1
        
    if lo <= hi:
        return [lo, hi]
                
    return [-1, -1]
'''