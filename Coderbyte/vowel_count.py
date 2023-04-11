# Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.

def VowelCount(strParam):


  contador = 0
  vogais = ['a', 'e', 'i', 'o', 'u']


  for char in strParam:
    if char in vogais:
      contador += 1
  
  return contador


# keep this function call here 
print(VowelCount(input()))
