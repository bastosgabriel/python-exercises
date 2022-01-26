import json

from data import words_list

letters_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for word in words_list:
    for letter in word:
        letters_count[letter] += 1

ordered_letters_count = {
    k: v for k, v in sorted(letters_count.items(), key=lambda item: item[1], reverse=True)}

with open("letters_count.txt", "w") as file:
    file.write(json.dumps(ordered_letters_count, indent=2, default=str))

print('-----------------------------------------------------------')
print('ordered_letters_count')
print()
print(json.dumps(ordered_letters_count, indent=2, default=str))
print()
print('-----------------------------------------------------------')
