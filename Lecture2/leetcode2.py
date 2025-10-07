############ LEET CODE ##############


'''125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

s = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x = s.lower().strip()
y = ""
for i in x:
    if i in alphabet:
        y = y + i

def isPalindrome(y):
    k = ""
    for i in y:
        k = i + k
    if y == k:
        return True
    else: 
        return False

print(isPalindrome(y))


# AI improved solution
def isPalindrome2(s: str) -> bool:
    x = ""
    for i in s.lower():
        if i.isalnum():
            x += i
    return x == x[::-1]
print(isPalindrome2("kalem"))