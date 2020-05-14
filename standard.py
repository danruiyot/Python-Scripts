numbers = [1,2,3,4,5,1,4,5] 
Sum = sum(numbers) 
count = len(numbers)

avarage = Sum / count
squared = 0

for number in numbers:
    first = number - avarage
    squared = first*first
    # print(number)

second = squared / count
final = second**(1/2.0)
print(final) 