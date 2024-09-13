letter = "Hey my name is {0} and I am from {1}"
country = "India"
name = "Rishabh"


print(letter.format(name, country))
# This method is very hard

# And so we use "new formatting Strings (by PEP 498)"

print(f"Hey my name is {name} and I am from {country}")
country = "India"
name = "Rishabh"

# Hard way-

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.999999)) # Does the round-off

# Mentos way-

price = 49.999999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}") # 60
print(type(f"{2 * 30}")) # <class 'str'>