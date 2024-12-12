#question1 ii

list = [4,7,2,9,12,15]
sum_of_odd_numbers = 0

for numbers in list:
    if numbers %2 != 0:
        sum_of_odd_numbers+=numbers
print(f" The sum of the odd numbers is equal to: {sum_of_odd_numbers}")