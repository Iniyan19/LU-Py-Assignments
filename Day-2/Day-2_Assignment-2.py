#find if prime or not
import math

number = int(input("Enter an Integer : \n"))
#number is a prime number only if it has its factors as 1 and the number itself
#10
flag =0
if number == 0:
    print("0 is neither prime nor composite number.")
else:
    for num in range(1,math.floor((number+1)/2)):
        if(number%num==0):
           flag = flag+1
if(flag>1):
    print("Not prime")
else:
    print("prime number")
        
