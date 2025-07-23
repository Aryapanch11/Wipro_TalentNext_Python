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
    print("not a pallindrome no.")