first = int(input("Welcome to the calculator! Type any integer:"))
second = int(input("Okay. Now type another interger:"))
third = (input("Answer with these keywords only - +, -, *, /? Answer:"))

if third == "+":
    print(first + second)
elif third == "-":
    print(first - second)
elif third == "*":
    print(first * second)
elif third == "/":
    print(first / second)
else:
    print("Invalid Value!")
