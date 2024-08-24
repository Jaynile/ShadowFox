"""Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the
result. Try to identify the representation used."""

def format_string(number, char):
    formatted_string = "The number is {} and the character is '{}'".format(number, char)
    return formatted_string
result = format_string(145, 'o')
print(result)
