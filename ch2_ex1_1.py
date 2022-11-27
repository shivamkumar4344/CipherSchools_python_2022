# Two or more inputs in one line
name,age = input("Enter the name and age:-").split(",")
print(name)
print(age)
# String Formatting
name = "Shivam"
age = 19
print("Your name is "+name+" and Your age is "+str(age))#Python2

print("Your name is {} and Your age is {}".format(name,age))#Python3

print(f"Your name is {name} and Your age is {age}")


# Excersice question
#Ask user to input three numbers and you have to print average of three no. using string formatting.
num1 = 90
num2 = 87
num3 = 97
avg = int(num1+num2+num3)/3
print(f"Numbers are {num1},{num2},{num3} and their average is {avg}.")