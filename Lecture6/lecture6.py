# Write code to bisection search to find the cube root of positive cubes within some epilson
cube = 27
epilson = 0.01
num_guesses = 0
low = 0
high = cube

if cube >= 1.0:
    low = 1.0
    high = cube
else:
    low = cube
    high = 1.0
guess = (high + low)/ 2.0

while abs(guess**3 - cube) >= epilson:
    if guess**3 < cube:
        # guess to low
        low = guess
    else:
        # guess to high
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

print(num_guesses)
print(guess, "is close to",cube )

        