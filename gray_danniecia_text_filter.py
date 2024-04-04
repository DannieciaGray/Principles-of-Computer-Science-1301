'''
Description: This code will define a function named text_filter() that takes a string as a parameter,
representing the message that is about to be sent, and returns a new string that has the words in the list
of banned words removed. Then, write a main program that reads the message string as an input, calls
the text_filter() with the input as an argument, and outputs the new filtered text.

For this program,the banned words list will only contain the following 5 words.
1. Turkey
2. Dog
3. Fox
4. Cat
5. Chicken

Author: Danniecia
'''

def text_filter(message):

    banned_words=["Turkey","Dog","Fox","Cat","Chicken"]

    for i in range(len(banned_words)):

        if banned_words[i] in message:
            message=message.split()
            message.remove(banned_words[i])
            return(" ".join(message))
            

messages=input("Enter a text: ")
print(text_filter(messages))

