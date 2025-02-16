# f,formatted string literals
# Yeh strings ke andar variables ko embed karne ka easy tareeqa hai.
# 🔥 Example 1: f-string vs Normal Concatenation

# 🔸 Without f-string (Concatenation Method)
name= "Amairah"
age= 21
print("my name is "+ name + " and I'm " + str(age) + " years old")  #extra use of str(age)

# 🔹 With f-string (Easy & Clean)
name="amairah"
age=21
print(f"my name is {name} and my age is {age} years old.")  #Strings aur variables directly embed ho jate hain {} ke andar.
                                                            #Readable aur clean syntax hai.

# Challenge for You:
# Write a Python program that asks the user for their name and age, then prints the message using an f-string:
name=input("write your name ")
age=int(input("write your age "))
print(f"Hello {name} , you are {age} years old")

# split and strip methods in the above same code

user_input=input("enter your name and age (comma seperated):")
name,age=user_input.split(",") #splitting input by comma
print(f"your name is {name.strip()} and your age is {age.strip()}") #removes extra spaces before and after input
