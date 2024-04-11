import random

select = input("Enter whether you want heads(H) or tails(T): ")

if select.upper() == 'H':
    new = random.randint(0, 1)
    if new == 0:
        print("Congratulations! You won the toss.")
    else:
        print("Sorry! You lost the toss.")
elif select.upper() == 'T':
    new = random.randint(0, 1)
    if new == 1:
        print("Congratulations! You won the toss.")
    else:
        print("Sorry! You lost the toss.")
else:
    print("Invalid input. Please enter either 'H' or 'T'.")
