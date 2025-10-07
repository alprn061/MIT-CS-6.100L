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
