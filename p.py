x = int(input("What's the value of x? "))
if x < 2:
    print(f"{x} is not a prime number")
else:
    for i in range(2,x):
        if x % i == 0:
            print(f"{x} is not a prime number")
            break
    else:
        print(f"{x} is a prime number")