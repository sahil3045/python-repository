# we are going to take a input from user in form of a sentence and then ask the user which word he wants to change and then print the edited sentence. 
sen = input("Enter your Sentence: ")
print("Your sentence is ", sen)
word1 = input("Enter the word you want to replace: ")
word2 = input ("Enter the word you want to replace it with: ")
print(sen.replace(word1, word2))
