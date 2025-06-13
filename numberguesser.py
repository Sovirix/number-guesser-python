import random
attempts = 1
number = random.randint(1,10)
guess = int(input("guess a number "))
while guess != number:
    if guess < number:
        print("too low")
    else:
        print("too high") 

     
    guess = int(input("try again: "))
    
    attempts = 1 + attempts

print(f"you got it in {attempts} tries!")  