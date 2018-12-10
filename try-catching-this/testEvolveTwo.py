### strange code below - user must comment what each part does ###
### strange code below to comment out! ###

import os

for i in range(5):
    print("#" * 20 + " ERROR CATCHER 9000 & ByteChecker Combo Breaker" + "#" * 20)

try:
    print(fifteen / 0)
except Exception as e:
    print("Error occured... {}".format(e))


print("\n\nBut the code must go on!")

while True:
    try:
        fileName = input("Please enter a file name:")
        if os.stat(fileName):
            break
    except Exception as e:
        print("Error occured... {}".format(e))

print(os.stat(fileName))

def byteChecker(fileName, chunksize=4096):
    with open(fileName, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for bytes in chunk:
                    yield bytes
            else:
                break

for bytes in byteChecker(fileName):
    print(bytes)
