# Challenge:

# Use a dictionary comprehension to count the length of each word in a sentence.

sentence = "count the length of each word in this sentence"
words = sentence.split(' ')
length_dict = {word:len(word) for word in words}
print(length_dict)


# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

divisors = range(2,10)
divisibles = [number for number in range(1,1001) if True in [True for divisor in divisors if (number % divisor == 0)]]
print(divisibles)


# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

divisors = range(2,10)
highest_divisible_dict = {number:max([divisor for divisor in divisors if (number%divisor==0)]) for number in range(1,31) }
print(highest_divisible_dict)
