"""
Program Description: This program will write a program using the given dictionary of letters and point values that takes a word as input and
outputs the base total value of the word (before being put onto a board).


Author:Danniecia Gray
"""

# function created to make bag of words
def build_dictionary(word_list):
    word_dict={}
    for word in word_list:
        word= word.lower()  # converts to lowercase to prevent case sensitivity

        if word in word_dict:  # if the word is already present, increase it's frequency
            word_dict[word]+= 1
        
        else:
            word_dict[word] = 1
    
    return word_dict

# splits the words into a list
word_list = input("Enter a text: ").split()

# calls on build dictionary function 
word_dict= build_dictionary(word_list)

#sorts dictionary by key 
sorted_dict= sorted(word_dict.items())


#iterates over each tuple in the sorted list and returns them in pairs
for word, i  in sorted_dict:
    print(f"{word}-{i}")

