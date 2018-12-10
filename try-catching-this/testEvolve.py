### strange code below - user must comment what each part does ###
### must run this first to generate file ###

import random

print("Welcome to your ESCP fortune!")

f = open("anthonySays.txt", "w+")

promise = "I will get my {} and become {}!\n"

for i in range(10):
    if random.randint(1,10) > 5:
        f.write(promise.format("ESCP", "1337"))

f.close()

lineChecker = 0
with open("anthonySays.txt") as nf:
    lineChecker = sum(1 for lines in nf)



if lineChecker > 5:
    f = open("anthonySays.txt", "r")
    print("\n" + f.read())
    f.close()
else:
    print("\nI'm sorry, but your future is vague... maybe check out Automating The Boring Stuff with Python?")



