import random
print("Hello,\nLet's play the game \nHere you have 5 chances to predict the no.")
secret = random.randint(1,100)
print("You just need to predict the no. bet 1 to 100")
print(secret)
attempts = 1
while True:
    guess = int(input("Enter the secret no.:"))
    if guess in range(1,101):
        if guess == secret:
            print(f"Congrats, you have guessed the correct no in {attempts} attempts")
            break
        elif guess > secret:
            print("secret no is little bit smaller")
        elif guess < secret:
            print("secret no. is little bit higher")
        attempts += 1
    else:
        print("enter no. only bet 1-100")