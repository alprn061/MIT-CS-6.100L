'''3. Longest Substring Without Repeating Characters
Medium
Topics: premium lock icon
Hint
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
def lengthOfLongestSubstring(s: str) -> int:
    subst = []
    if s == "":
        return 0
    for i in range(len(s)):
        # i = 0,1, 2, 3, ..
        subst.append([s[i]]) # subs + s[0]: "a", s[1]: "b"
        for j in range(i+1, len(s)): # iterate after i'th index over s
            if s[j] in subst[i]: # if duplicate break
                break
            else:
                subst[i] += s[j] # if not duplicate append
    return max(map(len, subst)) # map function is get from ai!!

#print(lengthOfLongestSubstring("abcabcbb")) #ouput : 3
#print(lengthOfLongestSubstring("bbbbb")) # output : 1
#print(lengthOfLongestSubstring("pwwkew"))
#print(lengthOfLongestSubstring(""))    #output : 3

## runtime :1386 ms --> bad
# a good solution from community:
#
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength   

# another solution:
#   def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength        









'''1108. Defanging an IP Address
Easy
Topics
premium lock icon
Companies
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:
The given address is a valid IPv4 address.
'''

def defangIPaddr(address: str) -> str:
    address = address.replace(".", "[.]")
    return address

#print(defangIPaddr("1.1.1.1"))
#print(defangIPaddr("255.100.50.0"))
