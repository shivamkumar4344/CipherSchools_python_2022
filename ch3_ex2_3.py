# Count the number of letters in the input by the user
name = input("Enter the name:-")
temp_var = ""
i = 0
while i<len(name):
    if name[i] not in temp_var:
        temp_var +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
    
# for loop
for i in range(1,11):
    print(f"hello world : {i}")