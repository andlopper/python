#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

import re


def LongestWord(sen):


  palavras = sen.split()
  longa = ""


  for palavra in palavras:
    palavra = re.sub(r'\W+', '', palavra) #Remove caracteres nÃ£o alfanumÃ©ricos
    if len(palavra) > len(longa):
      longa = palavra


  return longa


# keep this function call here 
print(LongestWord(input()))
