n=int(input("enter a number greater than 1: "))
#n is the variable and you will be inputting numbers into
Match=True

for num in range(2,n):
#range of 2 and n, also a for loop
  n%num
#i guess to make it divisible
  if n%num==0:
  # if loop to
    Match=False
if Match:
  print("num is prime")
  # if false it will say num is prime

else:
  print("name is not prime")