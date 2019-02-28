letter = input("Enter a letter: ")
vowel = 'a', 'e', 'i', 'o', 'u'

if(letter in vowel):
  print("The letter is a vowel")

if(letter not in vowel and letter not in 'y'):
  print("The letter is a consonant")

if(letter == 'y'):
  print("Sometimes y is a vowel, others a consonant")
