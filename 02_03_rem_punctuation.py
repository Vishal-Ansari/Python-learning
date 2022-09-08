#question 3

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = input("Enter a string: ")

no_punc = ""
for char in str:
   if char not in punctuations:
       no_punc = no_punc + char

print("Punctuation Free String: ",no_punc)

print("arman ansari section N 200111212")