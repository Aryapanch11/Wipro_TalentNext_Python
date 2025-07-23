#Write a program to check if a given number is Positive, Negative or Zero.
n = int(input("enter a number"))
if n>0:
    print("postive number")
elif n==0:
    print("Zero")
else:
    print("negative number")

#Write a program to check if a given number is odd or even.
n = int(input("enter the number"))    
if n%2==0:
        print("Even number")
else:
    print("odd numbeer")

#  Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

n1 =int(input("enter the 1st number"))
n2 =int(input("enter the 2nd number"))
mod1 = n1%10
mod2 = n2%10
if mod1 == mod2:
    print(True)
else:
    print(False)
  
#  Write a program to print numbers from 1 to 10 in a single row with one tab space.   

n=1
for i in range(1,11):
    print(i, end="\t")
    
#  Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
n=23
for i in range(23,58):
    if i%2 ==0:
        print(i ,end="\n")

# Write a program to check if a given number is prime or not.
n= int(input("enter the number"))
count =0
for i in range(1,n+1):
    if n%i ==0:
       count +=1
if count ==2:
    print("Prime number")
elif count >2:
     print("Not a prime number")
else:
    print("Unity number")

# Write a program to print prime numbers between 10 and 99

for n in range(10,100):
    is_prime =True
    for i in range(2,n):
        if  n%i ==0:
            is_prime =False
            break
    if is_prime:
       print(n, end=' ')
      
      
# . Write a program to print the sum of all the digits of a given number.
n= int(input("enter the number"))   
sum=0 
while n>0:
    z = n%10
    sum +=z
    n = n//10
print(sum)
      
# . Write a program to print the sum of all the digits of a given number.
n= int(input("enter the number"))   
sum=0 
while n>0:
    z = n%10
    sum +=z
    n =n//10
print(sum)
      
# Q9. Write a program to reverse a given number and print.
n = int(input("enter the num"))
rev =0
while n>0:
    z = n%10
    rev = rev*10+z
    n =n//10
print(rev)

# Q10. Write a program to find if the given number is palindrom or not.
n = int(input("enter the num"))
copy =n
rev =0
while n>0:
    z = n%10
    rev = rev*10+z
    n =n//10
if rev ==copy:
    print("palindrome no.")
else:
    print("not a palindrome no.")

    