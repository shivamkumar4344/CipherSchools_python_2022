# if elif else statement

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Enter your age:"))
if 0<age<=3:
    print("Ticket Price: Free")
elif 3<age<=10:
    print("Ticket Price: 150")
elif 10<age<=60:
    print("Ticket Price: 250")
else:
    print("Ticket Price: 200")
   
# sum of first 10 natural nummbers
total = 0
i = 1
while i<=10:
    total+=i
    i+=1
print(f"sum of first 10 natural no.={total}") 

# sum of n natural numbers
total_sum = 0
i = 1
num = int(input("Enter your number:"))
while i<=num:
    total_sum+=i
    i+=1
print(total_sum) 

# You have given a number and you have find the sum of its digits.
n = input("Enter the number:-")
total = 0
i = 0
while i < len(n):
    total+=int(n[i])
    i+=1
   
print(total)
     