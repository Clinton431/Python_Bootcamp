# using pseudo random number generator
import random

# x = random.randint(1,6) #number btn 1 and 6 
# y = random.randint()
# print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

print(z)


cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)
print(cards)
