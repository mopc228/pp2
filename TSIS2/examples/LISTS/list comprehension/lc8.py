fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]    