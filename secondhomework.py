a = 1
odd_numbers = []

while a < 999:
    a += 2
    cube = a**3
    odd_numbers.append(cube)
#print(odd_numbers)
units = []
tens = []
hundreds = []
thousands = []
tens_of_thousands = []
hundreds_of_thousands = []
millions = []
tens_of_millions = []
hundreds_of_millions = []
for i in odd_numbers:
    i = i % 10
    units.append(i)
for i in odd_numbers:
    i = i % 100
    i = i // 10
    tens.append(i)
for i in odd_numbers:
    i = i % 1000
    i = i // 100
    hundreds.append(i)
for i in odd_numbers:
    i = i % 10000
    i = i//1000
    thousands.append(i)
for i in odd_numbers:
    i = i % 100000
    i = i//10000
    tens_of_thousands.append(i)
for i in odd_numbers:
    i = i % 1000000
    i = i//100000
    hundreds_of_thousands.append(i)
for i in odd_numbers:
    i = i % 10000000
    i = i//1000000
    millions.append(i)
for i in odd_numbers:
    i = i % 100000000
    i = i//10000000
    tens_of_millions.append(i)
for i in odd_numbers:
    i = i % 1000000000
    i = i//100000000
    hundreds_of_millions.append(i)
sum_num = []
index = 0
for i in units:
    all_sum = i + tens[index] + hundreds[index] + thousands[index] + tens_of_thousands[index] + hundreds_of_thousands[index] + millions[index] + tens_of_millions[index] + hundreds_of_millions[index]
    index = index + 1
    sum_num.append(all_sum)
result =[]
for i in sum_num:
    if i % 7 == 0:
        result.append(i)
print(result)
print(sum_num)

#print(len(sum_num))
#print(len(odd_numbers))
#print(len(units))