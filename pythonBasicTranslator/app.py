# Define a function called 'translate' that takes a single argument 'phrase'
def translate(phrase):
    # Initialize an empty string to store the translated result
    translation = ""

    # Loop through each letter in the input phrase
    for letter in phrase:
        # Check if the letter (converted to lowercase) is a vowel ('a', 'e', 'i', 'o', 'u')
        if letter.lower() in "aeiou":
            # If the vowel is uppercase, append 'G' to the translation
            if letter.isupper():
                translation = translation + "G"
            # Otherwise, append a lowercase 'g' for lowercase vowels
            else:
                translation = translation + "g"
        else:
            # If the letter is not a vowel, append the original letter to the translation
            translation = translation + letter

    # Return the fully constructed translation
    return translation


# Prompt the user to input a phrase and print the translated result
print(translate(input("Enter a phrase: ")))