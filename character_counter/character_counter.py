text = input("Enter a word: ")
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print("Character counts:", count)
print("Dictionaries store key-value pairs.")
print("Try longer words or phrases.")