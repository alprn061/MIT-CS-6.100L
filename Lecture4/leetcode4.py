'''412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''

def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1,n+1):
            if (i % 3)== 0 and (i % 5) == 0:
                i = "FizzBuzz"
            elif i % 3 == 0:
                i = "Fizz"
            elif i % 5 == 0:
                i = "Buzz"
            else:
                i = str(i)
            output.append(i)
        return output

print(fizzBuzz(15))



'''2520. Count the Digits That Divide a Number
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Example 1:
Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Example 2:
Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

Example 3:
Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
'''
def countDigits(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    for i in str(num):
         if num % int(i) == 0:
              count += 1
    return count

print(countDigits(1248))
