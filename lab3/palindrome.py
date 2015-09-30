#palindrome codes

#input a word
text = input("Input a word: ")

#to see the word in reverse
word_rev = reversed(text)

#to see if the word is a palindrome
if list(text) == list(word_rev):
  print("This is a palindrome")

else :
  print("This is not a palindrome")
