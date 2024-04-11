import random
date=int(input("enter how many people you want to add here"))
b=[]
for i in range(date):
    b.append(input("please enter your name"))
    
print(b)    
c=random.choice(b)
print(f"haii {c} you have to pay the bill")