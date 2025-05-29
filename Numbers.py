while True:
    x = int(input("How old are you? "))
    if x == "a number":
        print(f"{x} is a number")
        break
    else:
        print("Invalid input! Enter your age")


def add_numbers(x,y):
    return x + y
addition = add_numbers(7, 9)
print(addition)



def crime(case):
    return "cold" + case
casefile = crime("case1")
print(casefile)



i = 3 + 5 * 9
j = (8/2) + 6
print(i,j)
a = 40
b = 10
print(a + b)
print(a / b)
print(a // b)
print(a * b)
print(a ** b)
print(a % b)
print(a - b)
p = -4.7
r = abs(p)
print(r)
u = int(p)
print(u)
q = round(p)
print(q)
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x/y, 2)
print(z)
print("You are","doing great")
