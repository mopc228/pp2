string = input()
upper = sum(1 for i in string if i.isupper())
lower = sum(1 for i in string if i.islower())
print(
    f"This string contains {upper} upper case letters and {lower} lower case letters"
)