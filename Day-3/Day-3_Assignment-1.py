"""number = int(input("Enter a number : \n"))
sum = 0
for num in range(1 ,number+1):
    sum = sum+num
print(f"The sum of first {number} numbers is {sum}.")"""

"""flag = 1
count = 0
sum = 0
while flag == 1:
    num = int(input("Enter a number : \n"))
    if(num =="" or num ==0):
        break;
    else:
        sum = sum + num
        count=count+1
print(f"sum of {count} number is {sum}")"""

limit = int(input("Enter the value of n numbers to be added : \n"))
start=1
sum =0
while(start<=limit):
    num = int(input(f"Enter the numbers one by one-->{start} : \n"))
    sum = sum + num
    start+=1
print(f"sum of {limit} number is {sum}")    
        
