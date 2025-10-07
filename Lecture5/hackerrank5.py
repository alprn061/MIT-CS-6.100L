# ai help to solve this problem -- i was very close but i can only solve the problem for 1 digits, for 2 and 3 digits i could not solve

'''Print Function
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123..n

Example
n = 5
Output: 12345

Example
n = 11
Output: 1234567891011
'''
n =112
output = 0
for i in range(1, n+1):
    basamak = 0
    temp = i
    while temp > 0:
        temp //= 10
        basamak += 1
    output = output * (10 ** basamak) + i
print(output)