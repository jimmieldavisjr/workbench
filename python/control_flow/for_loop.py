import time

name = "jimmie"

for i in range(1, 11):
    print(i)

for i in range(10):
    print(i)

for i in range(1, 101, 20):
    print(i)

for letter in name:
    print(letter, end="😁")

for i in range(10, -1, -1):
    if i == 0:
        print("0\nCOMPLETE 👍")
    else:
        time.sleep(5)
        print(i)