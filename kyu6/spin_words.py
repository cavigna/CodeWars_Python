def spin_words(sentence):
    array = sentence.split()
    for i in range(len(array)):
        if len(array[i]) >= 5:
            array[i] = array[i][::-1]

    return ' '.join(array)


def spin_words1(sentence):
    array = sentence.split()
    return " ".join([array[i][::-1] for i in range(len(array)) if len(array[i]) >= 5])


print(spin_words('Welcomesss hell sanguche'))

""" 
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more
letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"

"""
