##### Strings
f = "a"
g = " b"
h = "3"
#print((f+g) * int(h))


s = "abc"
#print(f"len function : {len(s)}")

# Index of Strings
#print(f"first character of the string: {s[0]}")
#print(f"last charachter of the string : {s[-1], s[len(s)-1]}")

# Slicing to get Substring   [start:stop:step(default = 1)]
s = "abcdefgh"
#print(f"slicing 4th charachter to 5th: {s[3:5]}")
#print(f"slicing by increasing 2 steps: {s[::2]}")
#print(f"slicing 4th charachter to 5th by increasing 2 steps: {s[3:5:2]}")
#print(f"slicing by stepping from right to left: {s[::-1]}")
#print(f"slicing 5nd to 2nd by stepping from right to left: {s[4:1:-1]}")


# Strings are immutable, you can create new objects
k = "car"
# k[0] = "b" --- ERROR


##### INPUT/OUTPUT
#x = input("Type anything : ")
#print(x*5)

# input always return a str, must cast if working with numbers
#x = input("Type a number: ")
#print(x*5)

#num = int(input("Type a number :"))
#print(num*5)

# exercise - 
#verb = input("Choose a verb: ")
#print(f"I can {verb} better than you !\n{(verb +" ") *5} ")






##### CONDITIONS FOR BRANCHING

# Comparison

#print([(2<3), (2>3),(not 2>3), (2<3 and 2>3), (2<3 or 2>3)])


#secret = 4
#u = int(input("Guess a number between 0-10 :"))
#print(secret == u)


# IF
# if <condition> : 
#    <code>
# else:
#    <code>
#  <rest of program>     

# if <condition> : 
#    <code>
# elif <condition>:
#    <code>
# elif <condition>:
#    <code>
#  <rest of program>  
# 
# 
# # if <condition> : 
#    <code>
# elif <condition>:
#    <code>
# else:
#    <code>
#  <rest of program>    

secret = 4
u = int(input("Guess a number between 0-10 :"))
diff = secret - u
if diff > 3:
    print("Too low")
elif diff < -3:
    print("Too high")
elif diff == 0:
    print("You got it!")
else:
    print("Close")
