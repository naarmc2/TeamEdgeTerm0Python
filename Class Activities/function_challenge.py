import string

def count_spaces(text):
    count = 0
    for char in text:
        if char in string.whitespace:
            count +=1
    return count

def count_Characters(text):
    count = 0
    for char in text:
        count +=1
    return count

def count_UpperCase(text):
    count = 0
    for char in text:
        #or if char == char.upper()
        if char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            count+=1
    return count
    

def count_LowerCase(text):
    count = 0
    for char in text:
        if char == char.lower():
            count+=1
    return count

def count_Vowels(text):
    count = 0 
    for char in text:
        if char in 'aeiouAEIOU':
            count+=1
    return count

text = 'Hi, how are you? My name is Nathania.'
print(count_Vowels(text))

