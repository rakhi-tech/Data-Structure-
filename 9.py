def count_characters(text):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = digit_count = special_count = 0

    for char in text:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():  
            digit_count += 1
        else:  
            special_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special Characters:", special_count)


string = input("Enter a string: ")
count_characters(string)
