'''1945. Sum of Digits of String After Convert
You are given a string s consisting of lowercase English letters, and an integer k. 
Your task is to convert the string into an integer by a special process, and then transform it by summing its digits repeatedly k times.
More specifically, perform the following steps:
1.Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
2.Transform the integer by replacing it with the sum of its digits.
3.Repeat the transform operation (step 2) k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

Example 1:
Input: s = "iiii", k = 1
Output: 36
Explanation:
The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:
Input: s = "leetcode", k = 2
Output: 6
Explanation:
The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:
Input: s = "zbax", k = 2
Output: 8

Constraints:
1 <= s.length <= 100
1 <= k <= 10
s consists of lowercase English letters.
'''

# this example is taken from community, not solved by me
def getLucky(s: str, k: int) -> int:
    number = ''
    for x in s:
        number += str(ord(x) - ord('a') + 1)
        
    # Perform the transformation `k` times
    while k > 0:
        temp = 0
        for x in number:
            temp += int(x)  # Sum the digits of the current number
        number = str(temp)  # Convert the sum back to a string
        k -= 1
    return int(number)  # Return the final result as an integer
#print(getLucky("zbax",2))



'''202. Happy Number
Easy
Topics
premium lock icon
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 

Constraints:
1 <= n <= 231 - 1
'''
def isHappy(n, seen = None):  

    if seen is None:
        seen = []
    if n in seen:
        return False
    seen.append(n)
    sum = 0
    for i in str(n):
        sum += int(i)**2
    if sum == 1:
        return True
    else:
        return isHappy(sum, seen)    
        
#print(isHappy(19))
#print(isHappy(2))
# runtime: 7ms, memory: 12.5 mb 






'''118. Pascal's Triangle
Easy
Topics
premium lock icon
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
'''

def generate(numRows: int) -> list[list[int]]:
    return