# Use of count and len function
name,char = input("Enter the name and character:-").split(",")
print(f"Length of your name is{len(name)}")
print(f"character count:{name.lower().count(char.lower())} ")

# replace()
# find method()

sen = "He is at his home and he is eating his lunch"
print(sen.replace("is","was"))
print(sen.replace(" ","_"))

pos1 = sen.find("is")
pos2 = sen.find("is",pos1+1)
print(pos1)
print(pos2)

# center() method
name = input("Enter the name:-")
print(name.center(len(name)+4,"$"))