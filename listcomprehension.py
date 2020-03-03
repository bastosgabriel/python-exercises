# Find all of the numbers from 1-1000 that are divisible by 7

divisible_seven = [number for number in range(1,1001) if number % 7 == 0]
print(divisible_seven)


# Find all of the numbers from 1-1000 that have a 3 in them

numbers_with_three = [number for number in range(1,1001) if str(number).__contains__('3')]
print(numbers_with_three)


# Count the number of spaces in a string

string = "count the number of spaces in this string"
spaces = [char for char in string if char == ' ']
print(len(spaces))


# Remove all of the vowels in a string

string = "remove all the vowels in this string"
new_string_list = [letter for letter in string if letter.lower() not in ['a','e','i','o','u']]
new_string = ""

for index, character in enumerate(new_string_list):
    new_string += new_string_list[index]

print(new_string)


# Find all of the words in a string that are less than 4 letters

string = "find all the words in this string that are less than 4 letters"
words = string.split(' ')
small_words = [word for word in words if len(word) < 4]

print(small_words)