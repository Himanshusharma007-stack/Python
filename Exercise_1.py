# Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

def sum_or_add(a, b):
    if (a*b) > 1000:
        return (f"Addition be {a+b}")
    elif (a*b) <= 1000:
        return (f"Product be {a*b}")

a = int(input("Enter the first number"))
b = int(input("Enter the Second number"))

result= print(sum_or_add(a, b))