### FRACTIONS - APPROXIMATION METHODS

x = 36
epilson = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess ** 2 - x) >= epilson:
    guess += increment
    num_guesses += 1
print("num_guesses =", num_guesses)
print(guess, "is close to square root of", x)




# Add an extra stopping condition and check for why the loop terminated
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001  # try with 0.00001
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
if abs(guess**2 - x) >= epsilon:
    print(f'Failed on square root of {x}')
    print(f'Last guess was {guess}')
    print(f'Last guess squared is {guess*guess}')
else:
    print(f'{guess} is close to square root of {x}')
    