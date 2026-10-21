import moud
from moud import para_rect as para
from moud import area_circle as area


num=int(input("Enter the number"))
num2=int(input("Enter the number"))
result1=para(num,num2)
print(f'parameter of rectangle={result1}')
result=area(num)
print(f'area of circle={result}')

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result2 = moud.unique_list(numbers)

print("Unique list:", result2)