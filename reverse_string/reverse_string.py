text = input("Enter a word: ")
reversed_text = text[::-1]
print("Reversed word is:", reversed_text)
if text == reversed_text:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
print("Slicing makes reversing easy.")
print("Try other words too.")
print("Keep practicing slicing!")