# Count how many unique letters there are
s = "abcaaaaaa"
seen = ""
for char in s:
    if char not in seen :
        seen += char
print(len(seen))


# Guess-Check Perfect Square root with while loop
guess = 0
neg_flag = False
#x = int(input("Enter an integer: "))
x=8
if x<0:
    neg_flag=True
while guess **2 <x:
    guess += 1
if guess **2 == x:
    print("Square root of", x, "is", guess)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... Did you mean", -x, "?")


y = 4
for i in range(1,11):
    if i ==y:
        print("Your secret number is",i)
        break

found = False
for i in range(1,11):
    if i ==y:
        found = True
        break
        
if found:
    print("Your secret number is",i)
else:
    print("Not Found!")


# Guess-Check with for loop
cube = int(input("Enter an integer: "))

for guess in range(cube+1):
    if guess**3 ==cube:
        print("Cube root of", cube, "is", guess)

# Guess-Check with negative values
for guess in range(abs(guess)+1):
    if guess **3 == abs(cube):
        if cube < 0:
            guess = - guess
        print("Cube root of "+ str(cube)+ " is" + str(guess))

# Guess-Check little faster
for guess in range(abs(cube)+1):
    if guess ** 3 >= abs(cube):
        break
if guess **3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube<0:
        guess = -guess
    print("Cube root of" +str(cube)+" is"+ str(guess))