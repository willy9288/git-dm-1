import random

x = random.randint(1, 50)
# print(x)


<<<<<<< HEAD
for i in range(15):
=======
for i in range(5):
>>>>>>> dev

    y = int(input("請猜一個數字:"))

    if x == y:
        print("猜對了!!!")
        break

    else:
        if x > y:
            print("猜高一點!")
        else:
            print("猜低一點~~~")

if x != y:
    print(f"答案為:{x}")

else:
    print(f"猜了:{i+1}次")

<<<<<<< HEAD

=======
>>>>>>> dev
print()
