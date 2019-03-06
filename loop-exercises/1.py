word = str(input("Enter your word: "))
vowel = 'a', 'e', 'i', 'o', 'u'
for letter in word:
  if letter not in vowel:
    print(letter)
