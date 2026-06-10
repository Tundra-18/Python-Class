def count_vowels(string):
    return sum(1 for char in string if char in 'AEIOUaeiou')

print(count_vowels(input("String: ")))

