lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
count=0
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           count+=1
 
print("Number of prime numbers in the given range:")        
print(count)
