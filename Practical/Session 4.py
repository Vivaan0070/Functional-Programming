# Write your exercise solutions here

# 1.
user_input = input("Enter a string: ")
number_of_vowels = 0

for char in user_input.lower():
    if char in 'aeiou':
        number_of_vowels += 1

print("Number of vowels in the string:", number_of_vowels)

# 2.
first_user_input = input("Enter the first string: ")
second_user_input = input("Enter the second string: ")

print("the concatenated string is:", first_user_input + " " + second_user_input)