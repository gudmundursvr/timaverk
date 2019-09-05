number1 = 0
number2 = 1
number3 = 0

n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(n):
    number_sum = number1+number2+number3
    number1 = number2
    number2 = number3
    number3 = number_sum
    print(number_sum)