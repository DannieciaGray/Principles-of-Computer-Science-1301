"""
Program Description: This program will write a program using the given dictionary of letters and point values that takes a word as input and
outputs the base total value of the word (before being put onto a board).


Author:Danniecia Gray
"""

# dictionary of scrabble words and their points
def word_to_points(word):
    scrabble_points = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10}

    points=0
    word = word.upper()

    # gets the value of the letter in word

    for i in range(len(word)):
        if word[i] in scrabble_points:
            points+= scrabble_points.get(word[i])

    return points
    

# while loop that keeps asking the user to enter a word unless they enter "q","Quit","quit"

while True:
    word = input("Enter a word: ")


# stops code when user enters any of the following
    if word == "q" or word == "Quit" or word == "quit":
        break

# returns points for scrabble word 

    else:
        print(word, "is worth", word_to_points(word) , "points.")
