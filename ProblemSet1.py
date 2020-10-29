""" QUESTION 1:
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any lower case letter for the 'd', so "cope" and "cooe" count. While writing your code, do not think only of given cases. These cases are just examples of testing your code. Your algorithm should cover more cases. You can use built-in functions.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
  count = 0
  for i in range(len(str)):
    word = str[i:i+4]
    if word[:2] == 'co':
      if word[3] == 'e':
        count+=1
  return count

""" QUESTION 2:
Write a function vowels(word) that uses the count method to return the number of vowels in the string word. Note that word may contain upper and lower case letters. You should not count Y as a vowel.

vowel('shorty') → 1
vowel('LONGER') → 2
vowel('a string with spaces AND $') → 6
"""
def vowel(string):
  lowString = string.lower()
  count = 0
  for char in lowString:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
      count += 1
  return count

""" QUESTION 3:
In data analytics, it is very common for data to come to us in a dirty form, with errors related to how it was transcribed or downloaded. Since we know any sequence of dna must consist of the four bases 'a', 'g', 't', 'c', any other letters appearing in dna must be a mistake. Write a function clean(dna) that returns a new DNA string in which every character that is not an A, C, G, or T is replaced with an N. For example, clean('goat') should return the string 'gnat'. You can assume dna is all lowercase, but don't assume anything about the nature of the wrong characters (e.g. they could even have been accidentally transcribed as numbers).

clean('') → ''
clean('agct7ttczttctgactgcaacgggcaatatgtctctxtgtggattaaaaaaagagtgtcygatagcagcttctgaactggttacctgcc') → 'agctnttcnttctgactgcaacgggcaatatgtctctntgtggattaaaaaaagagtgtcngatagcagcttctgaactggttacctgcc'
clean('gtgagtaaattaaaattttnttgacttaggtcactaaptactttaaccaatataggbatagcgcacagacagataaaaattacagagtac') → 'gtgagtaaattaaaattttnttgacttaggtcactaantactttaaccaatataggnatagcgcacagacagataaaaattacagagtac'
"""
def clean(dna):
  index = 0
  result = dna
  print (result)
  for char in result:
    if (char != 'a' and char != 'g' and char != 't' and char != 'c'):
      print(index)
      result = result[:index] + 'n' + result[index+1:]
    index += 1
  return result

""" QUESTION 4:
Write a function findATG(dna) that returns a list of indices of all of the positions (indices) where the codon ATG begins in the given DNA string. Do not use the built-in index method or find method. Constructing the list of indices is very similar to what we have done several times in building lists to plot. Assume dna is all lowercase, and read through it from left to right.

findATG('agcttttcattctgactgcaacgggcaatatgtctctgtgtggattaaaaaaagagtgtctgatagcagcttctgaactggttacctgcc') → [29]
findATG('gtgagtaaattaaaattttattgacttaggtcactaaatactttaaccaatataggcatagcgcacagacagataaaaattacagagtac') → []
findATG('atgagtaaattaaaattttattgacttaggtcactaaatactttaaccaatataggcatagcgcacagacagataaaaattacagagatg') → [0, 87]
"""
def findATG(dna):
  indicesList = []
  for index in range(len(dna)):
    if dna[index:index+3] == 'atg':
      indicesList.append(index)
  return indicesList


""" QUESTION 5:
A palindrome is a word that is the same spelled forwards and backwards. Write a function called palindrome that takes a string parameter and returns True if the string is a palindrome and False otherwise.

palindrome('Mom') → True
palindrome('redivider') → True
palindrome('raDar') → True
"""
def palindrome(string):
  lowerString = string.lower()
  for i in range (len(lowerString)):
    if lowerString[i] != lowerString[len(lowerString)-i-1]:
      return False
    return True
    
def main():
  print(count_code('codexxcode'))
  print(vowel('LONGER'))
  print(clean('agtc777agtc'))
  print(findATG('atgagtaaattaaaattttattgacttaggtcactaaatactttaaccaatataggcatagcgcacagacagataaaaattacagagatg'))
  print(palindrome('redivider'))
main()