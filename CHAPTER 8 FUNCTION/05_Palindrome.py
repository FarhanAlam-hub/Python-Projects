def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not a palindrome")