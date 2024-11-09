# Even or odd assignment:
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# Convert a number to a string:
def number_to_string(num):
    return str(num)


# Vowel count:
def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for char in sentence:
        if char in vowels:
            count+= 1
    return count