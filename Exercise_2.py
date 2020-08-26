# Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
def sumNum(a):
    j= 0
    for i in range(0, a):
        sum= i+j
        print(f"Current Number {i} Previous Number {j} Sum: {sum}")
        j= i
z= int(input("Enter the Range of the Number you want to Iterate"))
sumNum(z)