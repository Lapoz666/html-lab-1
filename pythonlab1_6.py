#using reverse

word=input("Enter a string : ")
rev_word=reversed(word)
if list(word)==list(rev_word):
    print("palindrome")
else:
    print("not")

#using loop

word=input("Enter a string : ")
rev_word=""

for i in word:
    rev_word= i + rev_word

if word == rev_word:
    print("It is palindrome")
else:
    print("not palindrome")