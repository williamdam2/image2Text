
# creating an empty list
from cv2 import sqrt


lst = []
avg = float(input("Nhap trung binh :"))
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)

up =0 
for i in range(0,len(lst)):
    k = (lst[i]- avg)*(lst[i]- avg)
    up+=k

s = up/(n-1)
s = sqrt(s)
print(s)