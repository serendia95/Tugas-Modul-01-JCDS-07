# Fibonacci sequence

x = int(input("Input a number: "))

a = 0
b = 1
c = [a, b]
counter = 2

while counter < x:
    d = a + b
    c.append(d)
    a = b
    b = d
    counter += 1

print(f"{c}")