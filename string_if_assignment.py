# Python Coding Assignment: String Manipulation with if Clause

user_input = input("Enter a string: ")

lower_input = user_input.lower()

if "hello" in lower_input:
    print("Greeting detected!")
elif user_input == user_input[::-1]:
    print("This is a palindrome!")
elif user_input.isupper():
    print("Why are you shouting?")
elif len(user_input) > 10:
    print("That's a long string!")
else:
    print("Nothing special about this string.")
